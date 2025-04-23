
# How to Run

## Prerequisites

- Python 3.9
- Ensure all required libraries are installed (refer to `requirements.txt`)

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create and Activate Virtual Environment (Optional but recommended)**

   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Configure the .env File**

   - Create a `.env` file in the root directory of the project (see `.env.example` file).

## Running the Application

2. **Run the Flask Application**

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Additional Commands
- **Initialize the Database**

  ```bash
  flask db init
  ```

- **Create Database Migrations**

  ```bash
  flask db migrate -m "migration message"
  ```

- **Run Database Migrations**

  ```bash
  flask db upgrade
  ```


## Testing

- **Run Tests**

  ```bash
  pytest
  ```