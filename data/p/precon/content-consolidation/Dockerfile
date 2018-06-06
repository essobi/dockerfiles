FROM node:argon  
  
ENV DEBUG precon:*  
  
# Create app directory  
RUN mkdir -p /usr/src/precon/message-processors/content-consolidation  
WORKDIR /usr/src/precon/message-processors/content-consolidation  
  
# Install app dependencies  
COPY package.json /usr/src/precon/message-processors/content-consolidation  
  
COPY start.sh /opt  
  
RUN chmod +x /opt/start.sh  
  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/precon/message-processors/content-consolidation  
  
#CMD [ "node", "index.js" ]  
CMD ["/usr/local/bin/node", "/usr/src/precon/message-processors/content-
consolidation/index.js" ]

