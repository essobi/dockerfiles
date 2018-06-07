FROM postgres:10.3-alpine  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
RUN apk add --update --no-cache \  
sudo  
  
RUN mkdir -p /ssl  
ADD ssl/cert.key /ssl/cert.key  
ADD ssl/cert.crt /ssl/cert.crt  
  
ADD provision.sh /docker-entrypoint-initdb.d/provision.sh  
  
EXPOSE 5432  

