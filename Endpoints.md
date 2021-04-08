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

### ANSWERS API Stuff

Available endpoints for answers

Listing all answers regardless of the question

GET request for ALL answers

https://questionbox-torpedo-shark.herokuapp.com/answers/

adding an answer is just a little extra

POST request for answers

https://questionbox-torpedo-shark.herokuapp.com/questions/1/answers/add/ <-- This endpoint requires the pk of the question it is associated with

```JSON
# JSON
{
	"body": "This might be the answer"
}
output
{
  "id": 4,
  "body": "This might be the answer",
  "question": 1
}
```

Now adding and viewing all answers is nice but what if you want to view only the answers for a particular question? EASY!

https://questionbox-torpedo-shark.herokuapp.com/questions/1/answers/  <-- notice we use  the pk of the question then ask for the answers 

```JSON
# JSON
output
[
  {
    "id": 1,
    "body": "this is a damn answer",
    "question": 1,
    "author": {
      "id": 1,
      "username": "admin"
    }
  },
  {
    "id": 2,
    "body": "WHAT NOW HEROKU!!!",
    "question": 1,
    "author": {
      "id": 6,
      "username": "GrantV2"
    }
  },
  {
    "id": 4,
    "body": "This might be the answer",
    "question": 1,
    "author": {
      "id": 6,
      "username": "GrantV2"
    }
  }
]
```

### User API Stuff

Only one currently working end point, this will likely change as well

GET request for user

https://questionbox-torpedo-shark.herokuapp.com/user/1/ <-- this is the pk for the user you intend to grab information on

DELETE request for a user

https://questionbox-torpedo-shark.herokuapp.com/user/1/destroy/ <-- once again grabbing the user's pk and this will do a DELETE  

grabs this specified user by id

### Profile API Stuff

GET request for a particular profile

https://questionbox-torpedo-shark.herokuapp.com/profile-page/1/ <-- this grabs the profile information based on the pk given, Users and Profiles should have the same pk numbers but they hold different information, although they are related by a OneToOne.

PATCH request for a profile

https://questionbox-torpedo-shark.herokuapp.com/profile-page/1/update/ 

```JSON
# JSON
{
	"location": "Home!"
}
output
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "admin"
  },
  "first_name": "",
  "last_name": "",
  "bio": "A long time ago I was a fish, but now I am a shark!",
  "location": "Home!",
  "join_year": "2021-04-07",
  "img": null
}
```

Now if we wanted only the questions relative to this profile we can do that

GET request for ONLY the questions from this profile

https://questionbox-torpedo-shark.herokuapp.com/profile-page/1/questions/  <-- has pk for the profile that is being compared

```JSON
# JSON, example return for this request
[
  {																				<----
    "id": 1,																	 |
    "title": "what is love?",  								 |
    "body": "baby don't hurt me",							 |
    "author": {																 |
      "id": 1,																 | One whole question
      "username": "admin"											 |
    },																				 |
    "tags": "tagged",													 |
    "musicgenre": "Booty Bass"                 |
  },																		  <----
  {																				<----
    "id": 5,																	 |
    "title": "I am a test, beep boop",         |
    "body": "beep boop",										   |
    "author": {																 |
      "id": 1,																 | 2nd question for this
      "username": "admin"											 | profile, all questions
    },																				 | are going to present
    "tags": "tags",														 | this way
    "musicgenre": "Test"											 |
  }																				<----
]
```

