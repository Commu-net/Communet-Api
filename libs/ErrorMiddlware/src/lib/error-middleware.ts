import { Request, Response, NextFunction } from 'express';

interface ErrorMessage extends Error{
    message? : string,
    status? : number
}

const errorMiddleware = (err: ErrorMessage, req: Request, res: Response) => {

  err.status = err.status || 500
  console.log(err.message)
  err.message  = err.message || "Something went Wrong"
  res.status(err.status).json({
      success:false,
      message:err.message,
      stack:err.stack
      
  })
};


interface AuthRequest extends Request {
  user: object;
  
}

function authMiddleWare(req: AuthRequest, res: Response, next: NextFunction) {
  console.log("auth middleware" , req.user)
  if (req.user) {
    next();
  } else {
    return res.status(401).json({
      success: true,
      message: "unauthorized"
    });
  }
  
  return; 
}
export {errorMiddleware, authMiddleWare};
