# Color-Palettes-Backend
This is a straightforward backend program to build a web API using **Django's RESTful API framework**. The main objective is to create, manage, and share color palettes. 

# Automated API Documentation 
This app includes an API that enables programmatic interaction with the application. You can access the API documentation at ([http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/))].

# Key-Features:
- **Palette Creation and Management**: The web API allows users to create, update, delete, and share color palettes with different combinations of dominant and accent colors. Users can also give their palettes a name and choose whether they want to make them public or private. The web API supports CRUD operations for palette objects and uses unique IDs to identify them.
- **Authentication and User Accounts**: Users have the capability to log in and unlock enhanced functionalities. Notably, the registration process is omitted; solely a login mechanism is in place utilizing REST Framework's Browsable API authentication. Administrative privileges are granted to create users exclusively through the admin panel. Following this, users can then login and log out using the Browsable API interface.
- **Public Palette Browsing**: Users can explore a variety of public color palettes without the need to log in. But they can not access any private palettes.
- **Palette Creation and Customization**: Once logged in, users can produce new color combinations. They can create their unique color palettes, selecting 1 to 2 dominant  colors and 2 to 4 accent shades. These newly formed palettes will be automatically linked to the user's profile. In the case of an administrator, they possess the authority to assign users to newly crafted palettes.
- **Privacy Settings**: Palette creators have the option to publish their palettes to the public or keep them private. This level of control ensures that users can choose whether to share their creations with others or keep them exclusive.
- **Favorite Saving**: Users can mark other users' palettes as favorites, creating a collection of inspirational color schemes that they can refer to for future projects.
- **Search by Palette Name**: A search functionality allows users to locate specific palettes by their names. This convenient and effective search mechanism improves user experience and helps users find desired palettes easily. This is from the extra task. If the user goes to the search page, they will see an HTML page where there is a search box, In the search box, they can search the Name of the color palette. The backend will query the public records with that particular name, and display them in the same HTML page, if there is no record with that name, there will be a message showing.

# How to Use

Follow these steps to set up and run the project:

1. Clone the project repository from `https://github.com/phreak1703007/Color-Palettes-Backend`

2. Create a virtual environment:

3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install project dependencies from `requirements.txt`:

5. Perform database migrations:
   ```
    python manage.py makemigrations
    python manage.py migrate
   ```
6. Run the project:
    ```
    python manage.py runserver
     ```
7. Access the admin page: Open your web browser and navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

8. Create a superuser account:
   ```
     python manage.py createsuperuser
   ```
9. You're all set!

# Some JSON Object Examples for Request/Response:
1. **Browse public color palettes(GET)** : 
   ```
       http://127.0.0.1:8000/api/v1/palettes/
   ```
   Response:
   ```
     [
    {
        "id": 1,
        "dominant_color_1": "FFA500",
        "dominant_color_2": "8B4513",
        "accent_color_1": "FFD700",
        "accent_color_2": "FF6347",
        "accent_color_3": "FFFF00",
        "accent_color_4": "228B22",
        "name": "Autumn Leaves",
        "is_public": true,
        "favorites": [
            2
        ]
    },
    {
        "id": 5,
        "dominant_color_1": "000000",
        "dominant_color_2": "",
        "accent_color_1": "FFFFFF",
        "accent_color_2": "800080",
        "accent_color_3": "",
        "accent_color_4": "",
        "name": "Night Sky",
        "is_public": true,
        "favorites": []
    }
    ]
    ```
   This will give all the public records, even without login.
   
2. **LOGIN**: To login : `http://127.0.0.1:8000/api-auth/login`

   To logout: `http://127.0.0.1:8000/api-auth/logout`
3. **Create color palettes and Manage them as a USER**: (Must Login before creating)
```
  http://127.0.0.1:8000/api/v1/palettes/
```
Request: 
```
    {
        "dominant_color_1": "FFA500",
        "dominant_color_2": "8B4513",
        "accent_color_1": "FFD700",
        "accent_color_2": "FF6347",
        "accent_color_3": "FFFF00",
        "accent_color_4": "228B22",
        "name": "Autumn Leaves",
        "is_public": true,
        "favorites": [
            2
        ]
    }
```
Response:
```
    {
        "id": 1,
        "dominant_color_1": "FFA500",
        "dominant_color_2": "8B4513",
        "accent_color_1": "FFD700",
        "accent_color_2": "FF6347",
        "accent_color_3": "FFFF00",
        "accent_color_4": "228B22",
        "name": "Autumn Leaves",
        "is_public": true,
        "favorites": [
            2
        ]
    }
```
4. **Create color palettes and Manage them as an ADMIN**: (Must Login before creating):
```
  http://127.0.0.1:8000/api/v1/palettes/
```
Request: 
```
     
        "dominant_color_1": "000000",
        "dominant_color_2": "",
        "accent_color_1": "FFFFFF",
        "accent_color_2": "800080",
        "accent_color_3": "",
        "accent_color_4": "",
        "name": "Night Sky",
        "is_public": true,
        "user": 3,
        "favorites": []
    }
```
Response:
```
        "id": 5,
        "dominant_color_1": "000000",
        "dominant_color_2": "",
        "accent_color_1": "FFFFFF",
        "accent_color_2": "800080",
        "accent_color_3": "",
        "accent_color_4": "",
        "name": "Night Sky",
        "is_public": true,
        "user": 3,
        "favorites": []
    }
```
*If you log in as a USER, your newly created palette will be automatically associated with your account, but if you log in as an admin, you can associate any new palette for any user you want*. 

4. **Palette Searching by name** :
```
  http://127.0.0.1:8000/api/v1/palette-search/
```
If you go to this link, you will be redirected to this HTML page, where if you search any palette name by its name, it will fetch the related information about that palette. But it can only fetch the public ones, not the private plattes. 

![search](https://github.com/phreak1703007/Color-Palettes-Backend/assets/62479964/4b1fc8d4-c906-4547-97f1-bd016fc18d81)

But if there is no record with that particular name, there will be a message saying: "No palettes found with that name."



        
