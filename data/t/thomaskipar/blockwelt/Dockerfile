FROM node  
  
WORKDIR /root  
  
COPY package.json package.json  
COPY .bowerrc .bowerrc  
COPY bower.json bower.json  
  
RUN npm install bower -g  
RUN npm install --unsafe-perm  
  
COPY src/backend src/backend  
COPY src/frontend/app /root/src/frontend/app  
COPY src/frontend/css /root/src/frontend/css  
COPY src/frontend/example /root/src/frontend/example  
COPY src/frontend/favicon.ico /root/src/frontend/favicon.ico  
COPY src/frontend/index.html /root/src/frontend/index.html  
  
EXPOSE 9003  
CMD cd /root/; npm start  

