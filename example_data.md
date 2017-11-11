# Sample API data returns

### A route object - note that the geo data isn't necessarily correct here.

```json
{
    "url": "http://127.0.0.1:8000/routes/5a3ca9b7-190f-42f8-ab80-ce5b2f425319/",
    "id": "5a3ca9b7-190f-42f8-ab80-ce5b2f425319",
    "min_lat": 137.794958353043,
    "min_long": 137.794958353043,
    "max_lat": 34.7291145754279,
    "max_long": 34.7294320063985,
    "center_lat": 86.26203646423545,
    "center_long": 86.26219517972075,
    "user": "http://127.0.0.1:8000/users/admin/",
    "routeid": 5,
    "parentid": 2,
    "data": "{
        "type": "FeatureCollection",
        "features": [
          {
            "type": "Feature",
            "properties": {},
            "geometry": {
              "type": "LineString",
              "coordinates": [
                [
                  137.7949208021164,
                  34.72877950808085
                ],
                [
                  137.79496908187866,
                  34.72911457542792
                ],
                [
                  137.7949583530426,
                  34.72943200639853
                ],
                [
                  137.79495298862457,
                  34.72974502741189
                ],
                [
                  137.79491543769836,
                  34.72996987276032
                ],
                [
                  137.7944004535675,
                  34.72994782912574
                ],
                [
                  137.79421806335446,
                  34.7299081505687
                ],
                [
                  137.79426097869873,
                  34.72953781645119
                ],
                [
                  137.79424488544464,
                  34.72925124724527
                ],
                [
                  137.79427707195282,
                  34.72902639994197
                ],
                [
                  137.7942931652069,
                  34.72878832566001
                ],
                [
                  137.7942985296249,
                  34.72870014982601
                ],
                [
                  137.7945989370346,
                  34.728722193793324
                ],
                [
                  137.79483497142792,
                  34.728722193793324
                ],
                [
                  137.79493153095245,
                  34.728726602586086
                ]
              ]
            }
          }
        ]
    }",
    "atype": "R"
}
```

### A Sample run of the above route, by the admin user

Please note that here the route_id and the user are the fully qualified URLs to
those respective objects, this is to enforce the hyperlinked nature of the data.
I.e you should be able to follow those URL's to discover more data, rather than having
to contruct them yourself.

```json
{
    "url": "http://127.0.0.1:8000/runs/1/",
    "route_id": "http://127.0.0.1:8000/routes/5a3ca9b7-190f-42f8-ab80-ce5b2f425319/",
    "user": "http://127.0.0.1:8000/users/admin/",
    "timestamp": "2017-11-11",
    "run_time": 17
}
```

### A sample users, from following the user URL in the above run example.

Note that password hash has been redacted, as this info will not be present in production.

```json
{
    "username": "admin",
    "url": "http://127.0.0.1:8000/users/admin/",
    "age": 0,
    "weight": 0,
    "height": 0,
    "gender": "M",
    "country": "",
    "active": true
}
```
