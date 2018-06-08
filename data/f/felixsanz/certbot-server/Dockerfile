FROM alpine:latest  
  
MAINTAINER Félix Sanz <me@felixsanz.com>  
  
RUN apk add --no-cache --upgrade certbot  
  
RUN mkdir /srv/http  
  
WORKDIR /opt/certbot  
  
EXPOSE 8000  
CMD ["httpd", "-f", "-p", "8000", "-h", "/srv/http"]  

