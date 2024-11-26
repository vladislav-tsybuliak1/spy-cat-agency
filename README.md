# Spy Cat Agency API

The **Spy Cat Agency API** is a Django-based project for managing spy cats & their missions
## Installing

### Prerequisites

- Python 3.8+
- Install PostgreSQL and create db
- Docker

### Steps to Install Locally

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/vladislav-tsybuliak1/spy-cat-agency
    cd spy-cat-agency
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
4. **Create .env file and set up environment variables**:

    ```bash
    POSTGRES_PASSWORD=<your db password>
    POSTGRES_USER=<your db user>
    POSTGRES_DB=<your db>
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    PGDATA=/var/lib/postgresql/data
    SECRET_KEY=<your Django secret key>
    ```

5. **Run Migrations**:

    ```bash
    python manage.py migrate
    ```
6. **(Optional) Load data to db**:

    ```bash
    python manage.py loaddata spy_cat_agency.json
    ```
7. **Start the Server**:

    ```bash
    python manage.py runserver
    ```

## Run with Docker

### Steps to Run Using Docker

1. **Build the Docker Image**:

    ```bash
    docker-compose build
    ```

2. **Start the Services**:

    ```bash
    docker-compose up
    ```

3. **Access the API**:

    - The API will be available at `http://localhost:8000/`.


### API Endpoints

The API endpoints for the Spy Cat Agency are in a Postman collection.

- **Postman Collection**: [Spy Cat Agency API](https://www.postman.com/cryosat-candidate-46254616/0a17f66d-8999-44f1-9aca-40cd5b2f7ab3/collection/tlyw1b2/spycatsagency-api)


## Contact
For any inquiries, please contact [vladislav.tsybuliak@gmail.com](mailto:vladislav.tsybuliak@gmail.com).
