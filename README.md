# Point of Sale (POS) Backend API

A FastAPI backend prototype for a point-of-sale system. The application is organized into routers, Pydantic schemas, service classes, SQLAlchemy models, and a PostgreSQL database layer.

## Features represented in the API

- Product and inventory record management
- Supplier management
- Customer management
- Staff user accounts and login
- Sales processing
- Payment records
- Receipt records

## Technology stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL

## Project structure

```text
.
├── app/
│   ├── models/       # SQLAlchemy database models
│   ├── repositories/ # Database operations
│   ├── routers/      # HTTP endpoints
│   ├── schemas/      # Request and response schemas
│   └── services/     # Business logic
├── database.py       # SQLAlchemy engine and session setup
├── main.py           # FastAPI application entry point
└── README.md
```

## Prerequisites

- Python 3.10 or later
- PostgreSQL
- pip

## Local setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the application dependencies:

```bash
python -m pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary
```

Create a PostgreSQL database for the application. The current connection string is defined directly in `database.py`; update it to match your local PostgreSQL configuration before starting the API.

Start the development server from the repository root:

```bash
uvicorn main:app --reload
```

Open the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API route groups

| Route prefix | Purpose |
| --- | --- |
| `/products` | Product records |
| `/suppliers` | Supplier records |
| `/customers` | Customer records |
| `/users` | Staff accounts and login |
| `/sales` | Sales processing |
| `/payments` | Payment records |
| `/receipts` | Receipt records |

Use Swagger UI at `/docs` to inspect the request and response schemas and available operations.

## Important security and production notes

This is an educational backend project and should not be treated as production-ready.

- The database connection string is currently hard-coded in `database.py`. Move it to an environment variable before sharing or deploying the application, and never commit real database credentials.
- Configure authentication and authorization for protected operations before real use.
- Use a dedicated database user with only the permissions the application needs.
- Add migrations, automated tests, and stronger input/error handling before production deployment.
- Do not use real customer or payment information while experimenting with this prototype.

## License

No license is currently specified. Do not assume the repository is licensed for reuse.
