FROM terragontech/node:6.9  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ADD . /usr/src/  
RUN npm install && npm cache clean  
CMD npm start  

