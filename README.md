# CapstoneTestServer (FastAPI)

A minimal FastAPI server for testing user login, deck retrieval, and real-time card sharing via WebSockets. Designed to run on an AWS EC2 instance.

---

## Features

- Register users
- User login
- Retrieve decks for a user
- Real-time card sharing using WebSockets
- Minimal test-ready setup for deployment

---

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- SQLAlchemy
- Passlib (bcrypt)
- Pydantic

---

## Installation

1. SSH into your EC2 instance:

   ```bash
   ssh -i ~/.ssh/id_rsa ec2-user@35.90.238.16
   ```

2. Clone the repository (or upload files):

   ```bash
   git clone https://github.com/acc668/CapstoneTestServer
   cd testServer
   ```

3. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

   ---

   ## Running the Server

   Start the FastAPI Server:

   ```bash
   uvicorn test:app --host 0.0.0.0 --port 8000
   ```

  Visit the URL in your browser:

  ```bash
  http://ec2-35-90-238-16.us-west-2.compute.amazonaws.com:8000/docs
  ```
