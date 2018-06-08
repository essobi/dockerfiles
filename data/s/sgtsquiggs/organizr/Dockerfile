FROM sgtsquiggs/alpine.nginx:3.4  
MAINTAINER sgtsquiggs  
  
RUN \  
# install packages  
apk add \--no-cache \  
php5-curl \  
php5-json \  
php5-ldap \  
php5-pdo \  
php5-pdo_sqlite \  
php5-xml \  
php5-zip  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

