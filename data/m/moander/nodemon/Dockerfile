FROM node  
  
RUN npm install -g nodemon babel gulp eslint jshint browserify  
  
#RUN mkdir /app  
VOLUME /app  
  
WORKDIR /app  
  
CMD [ "nodemon", "-L", "--harmony", "." ]  

