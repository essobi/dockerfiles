FROM node:argon  
  
ENV DEBUG precon:*  
  
# Create app directory  
RUN mkdir -p /usr/src/precon/message-processors/hashtagify-content-hashtags  
WORKDIR /usr/src/precon/message-processors/hashtagify-content-hashtags  
  
# Install app dependencies  
COPY package.json /usr/src/precon/message-processors/hashtagify-content-
hashtags  
  
COPY start.sh /opt  
  
RUN chmod +x /opt/start.sh  
  
RUN npm install  
  
RUN apt-get update  
  
RUN apt install vim -y  
  
# Bundle app source  
COPY . /usr/src/precon/message-processors/hashtagify-content-hashtags  
  
#CMD [ "node", "index.js" ]  
CMD ["/usr/local/bin/node", "/usr/src/precon/message-processors/hashtagify-
content-hashtags/index.js" ]

