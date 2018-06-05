FROM sgtsquiggs/alpine.nginx:3.4  
MAINTAINER sgtsquiggs  
  
ENV PUBLIC_URL=http://localhost:80/  
  
RUN \  
# install packages  
apk add \--no-cache \  
php5-json \  
php5-pdo_sqlite  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

