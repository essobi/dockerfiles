FROM node:6.9-onbuild  
RUN npm install -g phantomjs  
COPY start.sh /start.sh  
  
VOLUME ["/usr/src/app"]  
EXPOSE 3000  
ENTRYPOINT ["bash", "/start.sh"]  

