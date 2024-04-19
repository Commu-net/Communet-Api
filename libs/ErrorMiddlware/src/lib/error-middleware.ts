import { Request, Response, NextFunction } from 'express';

interface ErrorMessage extends Error {
    message : string,
    status? : number
}

const errorMiddleware = (err: ErrorMessage, req: Request, res: Response) => {
    const status = err.status || 500;
    const message = err.message || "Something went Wrong";
    console.log("error middle")
    console.log(message);

    return res.status(status).json({
        success: false,
        message: message,
        stack: err.stack
    });

}

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
