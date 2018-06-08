FROM magnitus/node-app:4  
MAINTAINER Eric Vallee (eric_vallee@webificservices.com)  
  
ENV UID="1000"  
COPY ./index.js ${APP_DIR}/  
COPY ./package.json ${APP_DIR}/  
  
RUN finalize.sh  
  
RUN mkdir -p /etc/letsencrypt/live && chown -R $UID:$UID /etc/letsencrypt/live  
  
EXPOSE 8080  

