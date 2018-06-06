FROM node:alpine  
  
RUN npm install --save json-server  
RUN npm install -g nodemon  
  
WORKDIR /data  
VOLUME /data  
  
ADD server/* /data/  
  
EXPOSE 8000  
ADD run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD []  

