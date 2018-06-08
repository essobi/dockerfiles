FROM node:7.6.0-slim  
  
RUN npm install --silent -g gulp-cli  
RUN mkdir -p /images/src  
  
COPY ./config/package.json /images/package.json  
COPY ./config/gulpfile.js /images/gulpfile.js  
  
WORKDIR /images  
RUN npm install --silent  
  
CMD [ "gulp" ]

