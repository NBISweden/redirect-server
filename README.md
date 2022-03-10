# redirect-server

A small flask server that will redirect urls based on the requested host name. It is used behind a reverse proxy which will send requests to it. E.g. a Nginx server that responds to `*.meet.nbis.se` and will proxy the request to this flask server, while also passing along the requested host name in the request headers.

Example Nginx config:
```
server {
    listen 80;
    server_name *.meet.nbis.se;

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;

        proxy_pass http://redirect-server:5000;
    }
}
```

On the `redirect-server`, this docker container should be running on port 5000.

```
docker run -d -p 5000:5000 ghcr.io/NBISweden/redirect-server:latest
```
