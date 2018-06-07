FROM node:4  
#Install cordova and ionic  
RUN npm install -g cordova ionic  
  
#Install bower  
RUN npm install -g bower  
  
#Install unit testing stuff  
RUN npm install karma --save-dev  
RUN npm install karma-jasmine --save-dev  
  
RUN npm install -g karma-cli  
RUN npm install -g phantomjs  
RUN npm install karma-phantomjs-launcher --save-dev  
  
WORKDIR myApp  
EXPOSE 8100  
CMD ["ionic","serve"]  

