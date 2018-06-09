FROM ryanj/centos7-s2i-nodejs:6.0.0  
  
# Install app dependencies  
USER root  
  
RUN npm install -g ember-cli bower  
  
RUN chown -R 1001:0 /opt/app-root/src/  
  
USER 1001  
  
EXPOSE 4200  

