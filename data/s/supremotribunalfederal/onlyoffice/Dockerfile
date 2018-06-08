FROM onlyoffice/documentserver:4.0.1.34  
MAINTAINER Tomás Godoi <tomas.godoi@stf.jus.br>  
  
RUN sed -i
's/var[[:space:]]c_oAscSaveTimeOutDelay[[:space:]]=[[:space:]]5000/var
c_oAscSaveTimeOutDelay = 500/'
/var/www/onlyoffice/documentserver/server/DocService/sources/DocsCoServer.js  
  
COPY fonts /usr/share/fonts/truetype/extras  
COPY certs /certs

