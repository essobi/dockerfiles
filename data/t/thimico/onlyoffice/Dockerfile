FROM onlyoffice/documentserver  
MAINTAINER Thimico <thimico@gmail.com>  
  
COPY /config/nginx/onlyoffice-documentserver-docservice.conf
/etc/nginx/includes/onlyoffice-documentserver-docservice.conf  
  
RUN sed -i
's/var[[:space:]]c_oAscSaveTimeOutDelay[[:space:]]=[[:space:]]5000/var
c_oAscSaveTimeOutDelay = 500/'
/var/www/onlyoffice/documentserver/server/DocService/sources/DocsCoServer.js  
  

