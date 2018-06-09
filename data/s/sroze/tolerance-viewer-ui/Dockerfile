FROM node  
  
RUN npm install -g gulp bower  
  
WORKDIR /app  
  
COPY package.json /app/package.json  
RUN npm install  
  
COPY bower.json /app/bower.json  
RUN bower install --allow-root  
  
COPY . /app  
  
ENV UI_PORT 80  
EXPOSE 80  
CMD ["/app/docker/run.sh"]  

