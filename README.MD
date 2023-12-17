# Hey Hom's Real Estate API

The Hey Hom's Real Estate API is a RESTful web service built using Django and Django REST Framework. This API allows you to manage property listings on the Hey Hom real estate marketplace, providing CRUD (Create, Read, Update, Delete) operations. It includes user authentication with JWT (JSON Web Tokens) using `djangorestframework-simplejwt`.


## Features

-   **Property Listings:** Create, retrieve, update, and delete property listings.
-   **User Authentication:** Secure authentication using JSON Web Tokens.
-   **Validation:** Input validation for property data to ensure data integrity.

Certainly! Below is a README template based on the last message. You can customize it further based on the specific features and requirements of your Django project.

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**

2. **Navigate to the Project Directory:**
   ```bash
   cd your-repository
   ```

3. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (Optional):**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

   This will start the development server, and you can access your Django project at `http://127.0.0.1:8000/`.


## Endpoints Documentation

### Register Endpoint (`/register/`)

The `/register/` endpoint facilitates the registration of new users on the Hey Hom Real Estate API. To create a new user account, send a POST request to this endpoint with the following required attributes:

#### Endpoint Details

-   **Method:** `POST`
-   **URL:** `/register/`
-   **Content-Type:** `application/json`

#### Request Attributes

The request body must contain the following attributes:

-   **`username` (string):** The desired username for the new user.
-   **`email` (string):** The email address associated with the new user.
-   **`password` (string):** The chosen password for the new user.
	
#### Request Example
	POST /register/
	Content-Type: application/json

	{
	  "username": "john_doe",
	  "email": "john@example.com",
	  "password": "secure_password123"
	}

### Token Endpoint (`/token/`)

The `/token/` endpoint provides token-based authentication for users on the Hey Hom Real Estate API. It allows users to obtain a JSON Web Token (JWT) by providing valid credentials.

#### Endpoint Details

-   **Method:** `POST`
-   **URL:** `/token/`
-   **Content-Type:** `application/json`

#### Request Attributes

The request body must contain the following attributes:

-   **`username` (string):** The username associated with the user account.
-   **`password` (string):** The password for the user account.

#### Request Example
```
POST /token/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "secure_password123"
}
```
#### Using the Token

Include the obtained JWT in the Authorization header for subsequent authenticated requests:

httpCopy code

`Authorization: Bearer your_access_token_here`

### Property Endpoint (`/property/`)

The `/property/` endpoint serves as the main gateway for managing property listings on the Hey Hom Real Estate API. This RESTful endpoint supports standard CRUD (Create, Read, Update, Delete) operations, enabling seamless interaction with property data.

#### Endpoint Overview
-  **List:**  `/property/list/`
-  **Detail:** `/property/detail/<str:pk>/'`
-  **Create:** `/property/create/`  
-  **Update:** `/property/update/<str:pk>/`
-  **Delete:** `/property/delete/<str:pk>/`

### List Properties (`/property/list/`)

The `/property/list/` endpoint provides a list of all available properties or allows for filtered retrieval based on query parameters.

-   **Method:** `GET`
-   **URL:** `/property/list/`

#### Request Example

`GET /property/list/`

#### Response Example
```
[
	{
		"id":  2,
		"title":  "Beautiful House for Sales",
		"description":  "A stunning house with modern amenities",
		"price":  "500000.00",
		"location":  "123 Main Street, Cityville",
		"property_type":  "House",
		"bedrooms":  3,
		"bathrooms":  2,
		"square_feet":  2000,
		"available":  true
	}
]
```
### Property Detail View (`/property/detail/<str:pk>/`)

The `/property/detail/<str:pk>/` endpoint retrieves detailed information about a specific property identified by its unique identifier (`pk`).

-   **Method:** `GET`
-   **URL:** `/property/detail/<str:pk>/`

#### Request Example

`GET /property/detail/1/`

#### Response Example
```
{
	"id":  2,
	"title":  "Beautiful House for Sales",
	"description":  "A stunning house with modern amenities",
	"price":  "500000.00",
	"location":  "123 Main Street, Cityville",
	"property_type":  "House",
	"bedrooms":  3,
	"bathrooms":  2,
	"square_feet":  2000,
	"available":  true
}
```
### Create Property (`/property/create/`)

The `/property/create/` endpoint allows the creation of a new property by providing the necessary details.

-   **Method:** `POST`
-   **URL:** `/property/create/`
-   **Authentication:** Bearer Token in the Authorization header.

#### Request Example
```
POST /property/create/
Content-Type: application/json
Authorization: Bearer your_access_token_here

{
  "title": "Amazing House for Sales",
  "description": "A stunning house with modern amenities",
  "price": 500000,
  "location": "123 Main Street, Cityville",
  "property_type": "House",
  "bedrooms": 3,
  "bathrooms": 2,
  "square_feet": 2000,
  "available": true
}
```

### Update Property (`/property/update/<str:pk>/`)

The `/property/update/<str:pk>/` endpoint allows updating an existing property by specifying the property ID (`pk`) and providing updated information.

-   **Method:** `PUT`
-   **URL:** `/property/update/<str:pk>/`
-   **Authentication:** Bearer Token in the Authorization header.

#### Request Example
```
PUT /property/update/1/
Content-Type: application/json
Authorization: Bearer your_access_token_here

{
  "title": "Updated Modern Apartment",
  "price": 220000,
  "location": "456 Urban Street, Downtown",
  "bedrooms": 3
}
```

### Delete Property (`/property/delete/<str:pk>/`)

The `/property/delete/<str:pk>/` endpoint allows the deletion of a property identified by its unique identifier (`pk`).

-   **Method:** `DELETE`
-   **URL:** `/property/delete/<str:pk>/`
-   **Authentication:** Bearer Token in the Authorization header.

#### Request Example
```
DELETE /property/delete/1/
Authorization: Bearer your_access_token_here
```