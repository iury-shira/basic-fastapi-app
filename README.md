# Basic FastAPI app

In this project it's used the FastAPI Python framework to develop a simple backend application. This application provides endpoints to perform basic CRUD
operations on a SQLite relational database, and also has an user authentication mechanism, with JWT token and hashed user passwords stored within its DB.

## Installation and set up

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
A user has two options to interact with this application, one it's with its local machine (after cloning this repo with the 'git pull' command, an the other 
option it's to access the safe link 'https://zeuk4w.deta.dev/', since the app was also deployed into the DETA plataform.

If user choose the first option (run on local machine), after cloning this repo, they should have Python 3.6+ installed, go on the appropriate local directory, 
either run a Python virtual environment or open the project in a PyCharm IDE. If user prefer open the project as a .idea (PyCharm IDE) project, the next steps
can be skipped, since PyCharm already provides, by default, a running Virtual Environment within its integrated terminal.

To be able to execute the application locally, using other coding editors (for example Visual Studio Code), consider the next steps due to set a Python Virtual 
Environment:

```bash
python -m venv my-virtual-env
```

Next, the user should run this virtual environment:

On Windows, run:

```bash
my-virtual-env\Scripts\activate.bat
```

On Unix based SO, run:

```bash
source my-virtual-env/bin/activate
```

After these steps, user needs to the next command to install the project dependencies:

```bash
pip install -r requirements.txt
```

Finished the installation of the packages, user, still in a virtual env, needs to start the uvicorn server to run the application on localhost:8000 (by default):

```bash
uvicorn sql_app.main:app --reload
```

Now user can use its own browser to access localhost:8000/docs to have a nice and frinedly Swagger UI view of the application endpoints and make test requests. An 
alternative it's to use the Postman app to make the requests.

If the user choosed to access the link 'https://zeuk4w.deta.dev/', they can perform the tests and usage at 'https://zeuk4w.deta.dev/docs' or make the requests in 
Postman, using 'https://zeuk4w.deta.dev/' before the endpoints.

## Usage and testing

Currently, the application has the below endpoints:

- /login
- /data
- /user
- /message

The '/login' endpoint needs to be accessed with the 'POST' verb, passing as body parameters, the 'username' and 'password'. If user make a request passing valid credentials, 
they'll receive a reponse body (in JSON format) with a generated token. With this token, the user can access/make requests on the other endpoints, since they pass "Bearer <token>" 
on the the Authorization header value on the other requests. Without this mentioned token, it's not possible to access the othe endpoints, the user will receive an 401 
UNAUTHORIZED http response.

Considering the user has logged (passed the authentication route), they can make a simple GET request at '/data' endpoint and receive a simple message 'Acesso permitido para 
<username>'.

There are other requests a user can perform, for example a complete simple CRUD on messages database table. Each row (message) it's relationed with a user. So, in other words 
although a user can see (query) all messages, it's only possible to edit (PUT verb) and delete (DELETE verb) its own messages.

At least, with the '/user' endpoint, it's possible to see (query) all users stored in the database (but not their passwords) and also add a new user to the database.

## Contributing
Pull requests are welcome. There's a lot that can improve in this project, for example paginate the JSON responses, validate email user, implement unit tests, admin route, 
updating user's data, etc.
