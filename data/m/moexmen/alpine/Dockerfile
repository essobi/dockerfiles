FROM alpine:3.6  
ENV TZ Asia/Singapore  
ENV DOCKERIZE_VERSION v0.6.1  
RUN \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \  
&& apk --no-cache add ca-certificates tzdata curl \  
&& curl -OL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& adduser -S -h /app -u 10000 app  
  
WORKDIR /app  

