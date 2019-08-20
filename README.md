# API for FACE_DETECTION
 API for test

### Installation

Everpoint requires [Docker](https://www.docker.com/) to run.

```sh
$ cd face_detection_API
$ docker compose-up
```

### Usage:
##### Admin Page: 
In your web browser open: [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)
Login: *toren332*
Password: *mypass321*
                
1. Click `Objs`
2. Click `add Obj` (right-top corner)
3. Choose your `image` with faces
4. Click `save`
5. Click `your_image_name`
6. Click `Edited photo:` hyperlink
*7. `Profit!!!`*
                
----

##### REST API: 
1. Download your image to link as multipart form with key `original_photo` [http://0.0.0.0:8000/api/v1/photos/findface/](http://0.0.0.0:8000/api/v1/photos/findface/)
2. Wait
3. Get json response like 
```javascript
{
    "edited_photo":"link_to_your_edited_photo.jpg"
}
```
*4. `Profit!!!`*