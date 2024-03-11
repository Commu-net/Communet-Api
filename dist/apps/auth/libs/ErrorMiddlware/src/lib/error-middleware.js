var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
var error_middleware_exports = {};
__export(error_middleware_exports, {
  authMiddleWare: () => authMiddleWare,
  errorMiddleware: () => errorMiddleware
});
module.exports = __toCommonJS(error_middleware_exports);
const errorMiddleware = (err, req, res) => {
  const status = err.status || 500;
  const message = err.message || "Something went Wrong";
  console.log("error middle");
  console.log(message);
  return res.status(status).json({
    success: false,
    message,
    stack: err.stack
  });
};
function authMiddleWare(req, res, next) {
  console.log("auth middleware", req.user);
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
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  authMiddleWare,
  errorMiddleware
});
//# sourceMappingURL=error-middleware.js.map
