FROM node:9.6.1-alpine  
  
CMD [ "verdaccio" ]  
EXPOSE 4873  
HEALTHCHECK CMD netstat -ln | grep 4873 || exit 1  
VOLUME [ "/var/opt/verdaccio" ]  
WORKDIR /var/opt/verdaccio  
  
RUN adduser -DH nodeuser \  
&& npm update npm \  
&& npm install --global verdaccio \  
&& chown nodeuser:nodeuser /var/opt/verdaccio  
  
USER nodeuser  
  
COPY [ "./config.yaml", "/var/opt/verdaccio" ]  

