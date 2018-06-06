FROM node:5.1.0-wheezy  
  
RUN mkdir /app  
WORKDIR /app  
COPY ./client /app  
  
RUN npm i  
RUN npm i -g serve  
RUN ./node_modules/gulp/bin/gulp.js  
WORKDIR /app/out  
  
CMD ["serve"]  
  

