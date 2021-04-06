# Endpoints examples

### example POST request when adding a question

https://questionbox-torpedo-shark.herokuapp.com/questions/  <-- endpoint

```JSON
# JSON
{
    "title": "testing123",            <-- must use "     instead of  '   if not the last line, needs a comma
    "body": "test body",
    "tags": "tag"
}
output
{
    "id": 1,
    "title": "testing123",
    "body": "test body",
    "author": {
        "id": 1,
        "username": "admin"
    },
    "tags": "tag",
    "replies": [],
    "musicgenre": "Booty Bass"
}
```



### example PATCH request

https://questionbox-torpedo-shark.herokuapp.com/questions/1/  <-- endpoint, the "1" is the id of the question that we intend to PATCH

```JSON
# JSON
{
  "title": "A new title"
}
output
{
    "id": 1,
    "title": "A new title",
    "body": "test body",
    "author": {
        "id": 1,
        "username": "admin"
    },
    "tags": "tag",
    "replies": [],
    "musicgenre": "Booty Bass"
}
```



### example DELETE request

https://questionbox-torpedo-shark.herokuapp.com/questions/1/  <-- endpoint, the "1" is the id of the question we intend to DELETE

This returns a 204

```JSON
output
[]
```





