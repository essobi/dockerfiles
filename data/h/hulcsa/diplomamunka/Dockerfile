FROM node:wheezy  
  
# Bundle app source  
COPY . /src  
WORKDIR /src  
  
# Install app dependencies  
RUN cd /src; npm install; node_modules/bower/bin/bower --allow-root install
--config.interactive=false  
  
EXPOSE 8080  
CMD [ "node", "." ]  

