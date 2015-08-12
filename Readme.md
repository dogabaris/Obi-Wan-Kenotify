#Obi Wan Kenotify


* Response will be like
```javascript
/*
 /login
 */

{

    "username":"doga",
    "password":"doga",
    "id":1,
    "roles":[
        {
            "name":"AI",
            "id":1
        },
        {
            "name":"admin",
            "id":3
        }
    ]

}


/*
/create
*/

{

    "Post":{
        "content":"qqq",
        "id":19,
        "published_at":"2015-08-15 15:00:00",
        "tag_id":1,
        "title":"qqqqqqq",
        "user_id":1
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