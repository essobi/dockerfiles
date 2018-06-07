# node/IDS  
# VERSION 1.0.1  
FROM node:latest  
MAINTAINER Christopher Freitag <Christopher.Freitag@htw-berlin.de>  
  
EXPOSE 3000  
RUN mkdir IDS  
ADD / /IDS/  
WORKDIR /IDS/IDSapp  
RUN find -type f -exec sed -i 's/localhost/ids-auto.f2.htw-berlin.de/g' {} \;  
RUN rm -f app.js  
RUN mv -f Dockerapp.js app.js  
WORKDIR /IDS  
RUN npm install  
WORKDIR /IDS/IDSapp  
RUN npm install  
  
ENTRYPOINT [ "npm" , "start" ]

