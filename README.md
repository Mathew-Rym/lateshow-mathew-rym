# lateshow-mathew-rym
## Setting Up PostgreSQL Database

Follow these steps to set up your PostgreSQL database for this project:

---

### 1.  Create a PostgreSQL Database

1. **Switch to the PostgreSQL user and open the PostgreSQL shell:**

   ```bash
   sudo su - postgres
   psql
   ```

2. **Create a new database user (if you don’t already have one):**
   Replace `<myuser>` with your desired username and `<password>` with a strong password:

   ```sql
   CREATE USER <myuser> WITH PASSWORD '<password>';
   ```

3. **Create a new database and assign your user as the owner:**

   ```sql
   CREATE DATABASE late_show_db WITH OWNER <myuser>;
   ```

4. **Verify your database was created:**

   ```sql
   \l
   ```

---

### 2.  Connect to the Database in VS Code

1. Open the PostgreSQL extension in VS Code.

2. Enter the following details:

   * **Host:** usually `localhost`
   * **Port:** usually `5432`
   * **Username:** `<myuser>` (the one you created)
   * **Password:** `<password>`
   * **Database:** `late_show_db`

3. If you get an authentication error, reset the password in the PostgreSQL shell:

   ```sql
   ALTER ROLE <myuser> WITH PASSWORD '<password>';
   ```

---

## Create `.env`

In the project root, add a `.env` file. Make sure to replace `<username>`,`<password>`,`<database_name>` with the correct one:

```env
FLASK_APP=server/app.py
FLASK_DEBUG=True
FLASK_RUN_PORT=5555
FLASK_SQLALCHEMY_DATABASE_URI=postgresql://<username>:<password>@localhost:5432/<database_name>
FLASK_SQLALCHEMY_TRACK_MODIFICATIONS=False

SECRET_KEY=supersecretkey
```

---

## Install Dependencies

Use your virtual environment:

```bash
pipenv install && pipenv shell
```

---

## Database Migration & Seeding

```bash
# Apply migrations
flask db upgrade

# Seed data
python server/seed.py
```

---

## Run the Server

```bash
flask run
```

The API runs on [http://localhost:5555](http://localhost:5555)

---

## Auth Flow

| Step | Description |
|------|--------------|
| ✅ **Register** | `POST /register` with JSON `{ "username": "user_name_of_choice", "password": "yourpassword" }` |
| ✅ **Login** | `POST /login` with same credentials. |
| ✅ **Session** | A secure session cookie is set on login. Use this cookie to access protected routes like `/appearances` POST and `/episodes/<id>` DELETE. |
| ✅ **Logout** | `DELETE /logout` clears your session. |

---

## API Routes

| Route | Method | Auth Required? | Description |
|-------|--------|-----------------|-------------|
| `/register` | POST | ❌ | Register a user |
| `/login` | POST | ❌ | Log in and create session |
| `/check_session` | GET | ❌ | Check if session is valid |
| `/logout` | DELETE | ✅ | Log out user |
| `/episodes` | GET | ❌ | List all episodes |
| `/episodes/<id>` | GET | ❌ | Get single episode |
| `/episodes/<id>` | DELETE | ✅ | Delete episode |
| `/guests` | GET | ❌ | List all guests |
| `/appearances` | GET | ❌ | List all appearances |
| `/appearances` | POST | ✅ | Create an appearance |

---

##  Example Request & Response

**Register**
```http
POST /register
Content-Type: application/json

{
  "username": "user_name_of_choice",
  "password": "mypassword"
}

Response:
{
  "id": 1,
  "username": "user_name_of_choice"
}
```

**Login**
```http
POST /login
Content-Type: application/json

{
  "username": "user_name_of_choice",
  "password": "mypassword"
}

Response:
{
  "id": 1,
  "username": "user_name_of_choice"
}
```

---

## Using Postman

1. **Register:** Send a `POST` to `/register`  
2. **Login:** Send a `POST` to `/login` — Postman will store the session cookie automatically.  
3. **Authenticated Routes:** Send a `POST` to `/appearances` or `DELETE` to `/episodes/<id>` using the saved session cookie.  
4. **Check Session:** `GET /check_session` to verify you're still logged in.  
5. **Logout:** `DELETE /logout` to clear the session.

---

## GitHub Repo

[GitHub Repo Link Here] [git@github.com:Mathew-Rym/lateshow-mathew-rym.git]

# lateshow-mathew-rym
