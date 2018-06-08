FROM node:argon  
  
ENV DEBUG precon:*  
  
# Create app directory  
RUN mkdir -p /usr/src/precon/api  
RUN mkdir -p /data/db  
RUN mkdir -p /data/dumps  
WORKDIR /usr/src/precon/api  
  
# Install app dependencies  
COPY package.json /usr/src/precon/api  
COPY install-mongodb.sh /usr/src/precon/api  
COPY algolia-config.sh /opt  
  
RUN chmod +x /opt/algolia-config.sh  
  
VOLUME ["/opt/api/data"]  
  
RUN npm install  
  
RUN apt-get update  
  
RUN apt install vim -y  
  
## install mongodb  
RUN curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.2.6.tgz  
#COPY mongodb-linux-x86_64-3.2.6.tgz /opt/mongodb  
RUN tar -zxvf mongodb-linux-x86_64-3.2.6.tgz  
#COPY  
ENV PATH /usr/src/precon/api/mongodb-linux-x86_64-3.2.6/bin:$PATH  
  
# install pm2 by VS  
RUN npm install pm2@latest -g  
  
# Bundle app source  
COPY . /usr/src/precon/api  
  
RUN chmod +x /usr/src/precon/api/run-api.sh  
  
EXPOSE 3000 27017 37375 28017  
#CMD ["/usr/src/precon/api/mongodb-linux-x86_64-3.2.6/bin/mongod &"]  
#CMD [ "pm2", "start", "server.js" ]  
CMD [ "node","integrations.js"]  
#ENTRYPOINT bash /usr/src/precon/api/run-api.sh  

