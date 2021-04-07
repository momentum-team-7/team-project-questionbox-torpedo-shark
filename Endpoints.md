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

### example user token gen

first generate a user
https://questionbox-torpedo-shark.herokuapp.com/auth/users/

```JSON
# JSON
{
  "username": "NewAdmin",
  "password": "notsogoodpassword"
}
output
{
  "email": "",
  "username": "NewAdmin",
  "id": 3     <-- depends on how many users made prior to this
}
```

after this we need to get the Token for that user
https://questionbox-torpedo-shark.herokuapp.com/auth/token/login/

```JSON
# JSON
{
  "username": "NewAdmin",
  "password": "notsogoodpassword"
}
output
{
  "auth_token": "b9af6653516f2315251c440ba2d340e579b1a521" <-- example Token
}
```

Now whenever we need to use the Token for example on a POST request, instead of on the "auth" tab below the url we will switch it to "Bearer Token".
Token     b9af6653516f2315251c440ba2d340e579b1a521
PREFIX   Token

after that as long as the user's token meets the permissions check you should be good to go for authenticating



