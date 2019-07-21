Documentation link: https://courses18.docs.apiary.io/#reference

# Courses

Courses is a simple API allowing users to view courses and create the new ones.

## URLs

• /snippets/ - collection of courses

• /snippets/{snippet_id}/ - courses details

## • Get collection of courses
### Request

GET /snippets/
```
$ curl -i -H 'Accept: application/json' http://localhost:8000/snippets/
```

### Response

```
HTTP/1.1 200 OK
Date: Tue, 02 Jul 2019 08:06:08 GMT
Server: WSGIServer/0.2 CPython/3.6.2
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 758

[]
```

## • Get course details
### Request

GET /snippets/{snippet_id}/
```
$ curl -i -H 'Accept: application/json' http://localhost:8000/snippets/75/
```

### Response
```
HTTP/1.1 200 OK
Date: Tue, 02 Jul 2019 08:40:30 GMT
Server: WSGIServer/0.2 CPython/3.6.2
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 706
```

## • Create new course
POST /snippets/
### Request
```
$ curl -d "@data.txt" -X POST http://localhost:8000/snippets/
```
### Response

## • Delete course
DELETE /snippets/{snippet_id}/
### Request
```
$ curl -X DELETE http://localhost:8000/snippets/75/
```

### Response
```
HTTP/1.1 204 No Content
```

## Data types
### • Course

·id(integer): id of the course

·name(String): name of the course

·description(String): main information about the course

·logo(String): link of the logotype

·category(int): category of course

·branches(array[Branch])

·contacts(array[Contact])

### • Branch
·latitude(String): latitude of the courses place

·longitude(String): longitude of the courses place

·address(String): address of the courses

### • Contact
·type(int):
 
     1-phone

     2-facebook

     3-email

·value(String):value of the contact


### Testing commands: 
```
1)coverage run --source='.' --omit='*/migrations/*.py' manage.py test

2)coverage report -m
```
