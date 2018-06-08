FROM alpine:3.2  
MAINTAINER George Dernikos <geoder101@gmail.com>  
  
ENV DOCKER_CONTAINER=1  
COPY entrypoint.sh /usr/bin/entrypoint  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN apk update \  
&& apk add nodejs \  
&& npm update -g  
  
ENTRYPOINT ["entrypoint"]  

