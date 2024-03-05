/* eslint-disable @typescript-eslint/no-explicit-any */
import passport, { AuthenticateOptions } from "passport"; 
import {Request , Response , NextFunction, urlencoded} from "express"; 

import { ApiResponse, Apperror } from "@auth/utils";
import { User, userInterface } from "@auth/mongo";

interface AuthOptions extends AuthenticateOptions{
    accessType? : string,
    approvalPrompt? : string
}

const authGoogle = async (req: Request, res: Response, next: NextFunction) => {
    try {
        passport.authenticate('google', {
            scope: ["profile" ,"email","https://www.googleapis.com/auth/gmail.compose"],
            accessType: 'offline',
            approvalPrompt: 'force'
        } as AuthOptions)(req , res , next);
        //     passport.authenticate('google', {
        //         scope:
        //             ['email', 'profile']
        //     }
        // )(req,res , next);
    }
     catch (error: any) {
        return next(new Apperror(error.message, 400));
    }
}

const googleCallback  =  (req : Request ,res : Response , next : NextFunction ) => {
    try {
        
        passport.authenticate("google", {
            successRedirect: `${process.env.DOMAIN}/api/v1/user/auth/google/success`,
            failureRedirect: `${process.env.DOMAIN}/api/v1/user/auth/google/failure`,
        })(req, res, next);
    } catch (error : any) {
        return next(new Apperror(error.message , 400));
    }
}

const googleSuccess = (req : any , res : Response , next : NextFunction ) => {
    try {
        console.log(req.user);
        const data = {
            email : req.user.email,
            name : req.user.name,
            picture : req.user.picture
        }   

        const queryString = Object.entries(data).map(([key, val]) => `${key}=${encodeURIComponent(val)}`).join('&');

        console.log(queryString);
        res.redirect(`${process.env.CLIENT_URL}?${queryString}`);

    } catch (error : any) {
        return next (new Apperror(error.message , 400));
    }
}



const googleFailure = (  req : Request, res : Response , next : NextFunction ) => {
    return next (new Apperror("You are not authenticated" , 400));
}


// interface RequestWithSession extends Request {
//     logout(arg0: (err: Error) => void): unknown;
//     user: any;
//     session: session.Session & Partial<session.SessionData> & { user?: any };
//   }
const logout = (req: any, res: Response, next: NextFunction) => {
    try {
        if (req.session) {
            req.session.destroy((err: Error) => {
              if (err) {
                console.log(err);
              }
              req.user = undefined;
            });
            req.logout((err: Error) => {
                if (err) {
                    console.log(err);
                }
            });
            return new ApiResponse(res , 200 , "Success" , {message : "You are logged out"});
          } else {
            req.logout((err: Error) => {
              if (err) {
                console.log(err);
              }
            });
            return new ApiResponse(res , 200 , "Success" , {message : "You are logged out"});
          }  
    } catch (error : any) {
        return next(new Apperror(error.message , 400));
    }
}



const getUserData = async (req : any , res : Response, next : NextFunction ) => { 
    const token = req.headers.authorization.split(" ")[1];
    console.log(token) 
    
    
    try {
        const user :userInterface = await User.findOne({sub : token});
        if (!user )  {
            return next(new Apperror("Error you are not Authenticated" , 400));
        }       
        return new ApiResponse(res , 200 , "Success" , user);
    
    } catch (error :any) {
        return next(new Apperror("Error you are not Authenticated" , 400));
    }
}




export  {
    authGoogle , googleCallback ,
    googleSuccess , googleFailure ,
    logout , getUserData
}