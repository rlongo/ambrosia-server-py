# Ambrosia Server

This project is meant to serve as the server for a personal digital recipe book.

## Running the App

dev environment: `python -m flask run`

The app can be run from the dockerfile. You just need to configure the following env variables:
* `DB_URL`: url of the database.
* `PORT`: which port to bind the web server to.

## Endpoints for `/api/v1`

### All Recipes

| Endpoint | Method | Summary |
|---|---|---|
| `/recipes?headers_only=true&tag=t1` | `GET` | Gets all recipes in the DB. Options to set tags to filter (any number) and whether you only want to return headers. |
| `/recipes` | `POST` | Bulk inserts full recipes. |

# Single Recipes

| Endpoint | Method | Summary |
|---|---|---|
| `/r` | `POST` | Adds a new recipes. This method takes only the recipe name as a param, and returns the `rid` which is used for future transactions on the recipe. |
| `r/<rid>` | `GET` | Fetches the recipe. |
| `r/<rid>/image` | `POST` | Uploads an image for the given recipe. |
| `r/<rid>` | `POST` | Updates metadata on the recipe (author, description, etc` |
| `r/<rid>/s/<sid>` | `PUT` | Updates the stage data for the given recipe. |
| `r/<rid>/s/<sid>/image` | `POST` | Uploads an image for the given recipe stage. |


