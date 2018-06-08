FROM onlyoffice/documentserver:4.3.2.3  
MAINTAINER Tomás Godoi <tomas.godoi@stf.jus.br>  
  
RUN sed -i 's/"savetimeoutdelay":[[:space:]]5000/"savetimeoutdelay": 500/'
/etc/onlyoffice/documentserver/default.json  
RUN echo 'localStorage.setItem("de-hide-right-settings", "1");' >>
/var/www/onlyoffice/documentserver/web-apps/apps/api/documents/api.js  
  
COPY fonts /usr/share/fonts/truetype/extras  
COPY certs /certs

