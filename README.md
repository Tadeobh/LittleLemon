# LittleLemon
Repository for the LittleLemon project from Coursera's Back-End Developer Capstone course, from the Back-End Developer certification.

## Endpoints

Please use the following endpoints to test this application:

### Menu Items

Use a GET request to get a list of all the Menu Items.
Use POST to add a new Menu item.
```
/restaurant/menu/
```

Use a GET request to get a specific Menu Item providing the ID (pk) of the object.
```
/restaurant/menu/<int:pk>
```

Make a POST request to this endpoint with 'username' and 'password' in the request Body to get an Authentication Token that you can use for endpoints that require authentication.
```
/restaurant/api-token-auth
```

To access Djoser's endpoints, please use ```/auth/``` as prefix (i.e. ```/auth/users/me```).