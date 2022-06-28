This script is an implementation of a HTTP RESTful Server to be used for learning and interviews in the team. Based on this: https://gist.github.com/miguelgrinberg/5614326

API Resources:
```
$ curl http://$HOST:5000/
$ curl -u 3ntr3v1st4:t3cn1c4 http://$HOST:5000/api/1.0.0/cms
$ curl -u 3ntr3v1st4:t3cn1c4 -X GET http://$HOST:5000/api/1.0.0/cms/appium
$ curl -u 3ntr3v1st4:t3cn1c4 -X GET http://$HOST:5000/api/1.0.0/cms/selenium
$ curl -u 3ntr3v1st4:t3cn1c4 -X GET http://$HOST:5000/api/1.0.0/cms/full
$ curl -u 3ntr3v1st4:t3cn1c4 -X GET http://$HOST:5000/api/1.0.0/rse
```

*cms* returns the full structure: appium, selenium dicts.
*cms/appium* returns the appium structure.
*cms/selenium* returns the selenium structure.
*cms/full* returns the full structure: appium, selenium dicts (same as cms).
*rse* returns the result of sencond exercise.

Installation instructions:
```
 pip install -r requirements.txt
```

Launch server: 
```
 python http_restful_server_functional.py
```


Launch docker:
```
    docker build -t interviews .
    docker run -p 5000:5000 interviews
```