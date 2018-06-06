FROM node:9.2.0  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY package.json /app/  
RUN yarn install --production  
COPY . /app  
  
COPY success-center-service_publishing /root/.ssh/id_rsa  
  
RUN chmod 600 /root/.ssh/id_rsa  
  
RUN ssh-keyscan -H github.com >> ~/.ssh/known_hosts  
  
RUN git config --global user.email "success-center-service@docker.com"  
RUN git config --global user.name "Success Center Bot"  
  
WORKDIR /app  
  
EXPOSE 80  
CMD [ "dumb-init", "node", "server.js" ]  

