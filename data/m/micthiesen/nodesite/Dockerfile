FROM google/nodejs  
  
EXPOSE 8080  
WORKDIR /app  
ADD package.json /app/  
RUN npm install  
ADD . /app  
RUN /app/node_modules/gulp/bin/gulp.js build  
  
CMD node server.js  

