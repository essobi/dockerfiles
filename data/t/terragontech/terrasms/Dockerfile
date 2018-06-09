FROM terragontech/node:6.9  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ADD . /usr/src/app  
RUN chmod +x /usr/src/app/run.sh  
RUN npm install && npm cache clean  
CMD sh run.sh  
  

