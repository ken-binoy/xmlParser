# FastAPI XML Parser

This is a simple **FastAPI** application that provides an API endpoint to parse XML data and return it as JSON.

## Features
- Accepts XML data via a `POST` request.
- Converts XML into a JSON format using `xmltodict`.
- Includes interactive documentation with Swagger UI and ReDoc.

---

## Prerequisites
1. Python 3.7+ installed on your system.
2. Install required libraries:
   ```bash
   pip install fastapi uvicorn xmltodict
