import { Request, Response, NextFunction } from "express";

interface ErrorMessage extends Error {
    message : string,
    status? : number
}

const errorMiddleware = (err: ErrorMessage, req: Request, res: Response) => {
    const status = err.status || 500;
    const message = err.message || "Something went Wrong";
    console.log("error middle")
    console.log(message);

    return res.set("Content-Type", "application/json").status(status).json({
        success: false,
        message: message,
        stack: err.stack
    });

}

export default errorMiddleware;