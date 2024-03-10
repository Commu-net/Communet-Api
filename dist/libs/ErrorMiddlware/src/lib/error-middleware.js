"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.authMiddleWare = exports.errorMiddleware = void 0;
const errorMiddleware = (err, req, res) => {
    const status = err.status || 500;
    const message = err.message || "Something went Wrong";
    console.log("error middle");
    console.log(message);
    return res.status(status).json({
        success: false,
        message: message,
        stack: err.stack
    });
};
exports.errorMiddleware = errorMiddleware;
function authMiddleWare(req, res, next) {
    console.log("auth middleware", req.user);
    if (req.user) {
        next();
    }
    else {
        return res.status(401).json({
            success: true,
            message: "unauthorized"
        });
    }
    return;
}
exports.authMiddleWare = authMiddleWare;
//# sourceMappingURL=error-middleware.js.map