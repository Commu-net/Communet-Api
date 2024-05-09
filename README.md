## Server local Installation

1. Clone the Repository ```bash git@github.com:Commu-net/Communet-Api.git ```

2. Install nx globally ```bash npm i -g nx ```

3. Build the containers for each Service. ```bash docker-compose up --build ```

4. User Endpoints
  


## Endpoints

### Home
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a link to the Google authentication route.

### Google Authentication
- **URL:** `/auth/google/`
- **Method:** `GET`
- **Description:** Initiates the Google authentication process. The scope of the authentication includes the user's profile, email, and the ability to compose Gmail messages. The access type is set to 'offline', and the approval prompt is set to 'force'.

### Google Authentication Callback
- **URL:** `/auth/google/callback/`
- **Method:** `GET`
- **Description:** Callback route for Google to call after authentication. If the authentication is successful, the user is redirected to the Google success route. If the authentication fails, the user is redirected to the Google failure route.

### Google Authentication Success
- **URL:** `/auth/google/success`
- **Method:** `GET`
- **Description:** Handles successful Google authentication. The user's email, name, sub, and id are returned as query parameters in a redirect to the client URL.

### Google Authentication Failure
- **URL:** `/auth/google/failure`
- **Method:** `GET`
- **Description:** Handles failed Google authentication. Returns an error message stating that the user is not authenticated.

### Logout
- **URL:** `/logout`
- **Method:** `GET`
- **Description:** Logs out the current user. If the user has an active session, the session is destroyed. The user is then logged out, and a success message is returned.

### Get User Data
- **URL:** `/getuser`
- **Method:** `GET`
- **Headers:** `Authorization: Bearer <token>`
- **Description:** Retrieves data for the current user. The user must be authenticated and provide a valid token in the Authorization header. If the user is found in the database, their data is returned. If the user is not found or not authenticated, an error message is returned.

5. Email Endpoints


## Base URL
The base URL for these endpoints is `http://localhost:/email`.

## Endpoints

### Send Mass Email with Attachments
- **URL:** `/send`
- **Method:** `POST`
- **Description:** Send mails with attachments.
- **Request Body:**
  - `emails`: Array of email addresses to send mails to.
  - `sender`: Email address of the sender.
  - `subject`: Subject of the email.
  - `text`: Body of the email.
  - Files to be attached.

### Manage Email
- **URL:** `/mail`
- **GET Method:** `GET`
- **Description:** Get all emails associated with a user.
- **Query Parameters:**
  - `userEmail`: Email address of the user.
- **POST Method:** `POST`
- **Description:** Add new email(s) to a user's account.
- **Request Body:**
  - `userId`: ID of the user.
  - `data`: Array of email objects containing the following fields:
    - `email`: Email address.
    - `currentDesignation`: Current designation (optional).
    - `name`: Name (optional).
    - `company`: Company (optional).
- **DELETE Method:** `DELETE`
- **Description:** Remove an email from a user's account.
- **Request Body:**
  - `userId`: ID of the user.
  - `_id`: ID of the email to remove.
- **PUT Method:** `PUT`
- **Description:** Update an existing email associated with a user.
- **Request Body:**
  - `userId`: ID of the user.
  - `data`: Object containing the following fields:
    - `_id`: ID of the email.
    - `email`: Email address.
    - `currentDesignation`: Current designation (optional).
    - `name`: Name (optional).
    - `company`: Company (optional).

### Store Mail
- **URL:** `/mail/store-mail`
- **Method:** `POST`
- **Description:** Store email(s) in a user's account.
- **Headers:** `Authorization: Bearer <token>`
- **Request Body:**
  - `emails`: Array of email addresses to store.