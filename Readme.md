#Obi Wan Kenotify


* Response will be like
```javascript
/*
 /login
 */

{

    "Profile":{
        "id":1,
        "password":"doga",
        "roles":[
            {
                "id":1,
                "name":"AI"
            },
            {
                "id":3,
                "name":"admin"
            }
        ],
        "username":"doga"
    }

}


/*
/create
*/

{

    "Post":{
        "content":"Response Test Content",
        "id":56,
        "published_at":"26.08.2015 15:00",
        "tag":{
            "id":1,
            "name":"AI"
        },
        "title":"Response Test",
        "user":{
            "id":1,
            "username":"doga"
        }
    }

}

/*
 /birdenfazlapost
 */

{

    "Posts":[
        {
            "content":"Test",
            "id":1,
            "published_at":0,
            "tag_id":1,
            "title":"test",
            "user_id":1
        },
        {
            "content":"Test Content",
            "id":2,
            "published_at":0,
            "tag_id":1,
            "title":"Test post",
            "user_id":2
        },
        {
            "content":"testcontent",
            "id":3,
            "published_at":0,
            "tag_id":1,
            "title":"testpost",
            "user_id":1
        }
    ]

}
```
