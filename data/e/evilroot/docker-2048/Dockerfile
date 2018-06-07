FROM alpine:latest  
  
MAINTAINER evilroot <k@e-dot.pl>  
  
RUN apk --update add nginx  
  
COPY 2048 /var/lib/nginx/html  
  
LABEL env=prod  
  
CMD ["nginx", "-g", "pid /tmp/nginx.pid; daemon off;"]  

