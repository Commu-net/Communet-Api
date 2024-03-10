import { Router } from "express";

import { getAllEmail  , sendMass , addEmail, removeEmail , updateEmail, storeMail} from "../controllers/email.controllers";

const router: Router = Router();



router.route("/send").post(sendMass);  //send mails with attachments 


router.route("/mail")
                    .get(getAllEmail)
                    .post(addEmail)
                    .delete(removeEmail)
                    .put(updateEmail);

router.route("/mail/store-mail")
    .post(storeMail);


export default router;

