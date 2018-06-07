FROM dockerfile/nodejs  
  
ADD . /scaffold  
RUN npm install -g nodemon  
WORKDIR /scaffold  
RUN rm -rf .git  
RUN npm install  
  
WORKDIR /app  
  
CMD mv /scaffold/* . && nodemon ./index.js localhost 8080  
  
EXPOSE 8080

