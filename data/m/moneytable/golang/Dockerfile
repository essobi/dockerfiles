FROM golang:1.8.3-alpine  
  
MAINTAINER Metz Charusasi <metz@moneytable.com>  
  
ENV APP_BIN main  
ENV APP_ARGS ""  
ENV DOCKERIZE_VERSION v0.5.0  
RUN apk update && apk upgrade && \  
apk add --no-cache bash curl git openssh openssl  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN go get github.com/tools/godep  
RUN go get github.com/codegangsta/gin  
ADD app.sh /app.sh  
  
CMD ["/bin/sh", "/app.sh"]  

