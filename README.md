## Docker for Mac Native Crashing on Heavy IO

To reproduce https://github.com/docker/hyperkit/issues/50 follow this:

```bash
git clone git@github.com:bryanhelmig/docker-compose-crash-repro.git
cd docker-compose-crash-repro
docker-compose build
docker-compose up -d
docker-compose logs -f -t web
```

Now visit `http://localhost:8888/` and do some *shift-click-refresh*ing - after a few times I fairly reliably get this:

```
web_1  | 2016-10-06T19:15:35.225908239Z [06/Oct/2016 19:15:35] "GET / HTTP/1.1" 200 60619
web_1  | 2016-10-06T19:15:35.690833698Z [06/Oct/2016 19:15:35] "GET /static/js/4.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:15:35.697437814Z [06/Oct/2016 19:15:35] "GET /static/js/5.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:15:35.747355583Z [06/Oct/2016 19:15:35] "GET /static/js/0.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:15:35.759419965Z [06/Oct/2016 19:15:35] "GET /static/js/1.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:15:35.837092723Z [06/Oct/2016 19:15:35] "GET /static/js/2.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:15:35.842664356Z [06/Oct/2016 19:15:35] "GET /static/js/3.js HTTP/1.1" 200 3005276
Unexpected API error for dockercomposecrashrepro_web_1 (HTTP code 500)
Response body:
dial unix /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/*00000003.00000948: connect: connection refused
```