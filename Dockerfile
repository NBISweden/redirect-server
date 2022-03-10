FROM alpine:latest

# install packages
RUN apk update ; apk add git py3-flask

# add startup script
COPY startup.sh /

ENTRYPOINT ["sh", "/startup.sh"]
