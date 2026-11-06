# ArticleManager - Django REST API for Article Management

## Project Description
ArticleManager is a RESTful API built with Django and Django REST Framework (DRF) for managing articles. The API supports the basic CRUD (Create, Read, Update, Delete) operations for articles and includes additional features such as filtering, pagination, and automatic generation of API documentation.

## Features
- **List all articles**: Retrieve a list of all articles in the system.
- **View article details**: View detailed information about a specific article.
- **Create an article**: Add new articles to the system.
- **Update an article**: Modify the details of an existing article.
- **Delete an article**: Remove articles from the system.
- **Data Validation**: Ensure that the title does not exceed 100 characters and content is not empty.
- **Filtering**: Filter articles by author or creation date.
- **Pagination**: Paginate the list of articles to handle large datasets.
- **API Documentation**: Automatically generated API documentation using Swagger/Redoc with drf-yasg.

## Technologies Used
- Django
- Django REST Framework
- Python
- PostgreSQL (or any database of your choice)
- drf-yasg for API documentation

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/Medamineelkhattabi/Django-REST-API.git
