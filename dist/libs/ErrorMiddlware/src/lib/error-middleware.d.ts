import { Request, Response, NextFunction } from 'express';
interface ErrorMessage extends Error {
    message: string;
    status?: number;
}
declare const errorMiddleware: (err: ErrorMessage, req: Request, res: Response) => Response<any, Record<string, any>>;
interface AuthRequest extends Request {
    user: object;
}
declare function authMiddleWare(req: AuthRequest, res: Response, next: NextFunction): Response<any, Record<string, any>> | undefined;
export { errorMiddleware, authMiddleWare };
