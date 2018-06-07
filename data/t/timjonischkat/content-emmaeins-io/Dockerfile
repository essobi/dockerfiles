FROM node:5.12.0  
MAINTAINER tim@emmaeins.io  
  
RUN apt-get install imagemagick  
  
ADD . /app  
WORKDIR /app  
  
RUN rm -rf cache && mkdir cache && chmod 0777 cache  
  
RUN npm install && node_modules/.bin/gulp  
  
CMD ["npm", "start"]

