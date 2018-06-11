FROM alpine:latest  
MAINTAINER LM <treerootboy@gmail.com>  
  
RUN apk update  
RUN apk add nginx-lua  
  
EXPOSE 80  
EXPOSE 443  
RUN adduser -u8080 -D -H www  
  
VOLUME /www  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
CMD nginx -g 'daemon off;'  

