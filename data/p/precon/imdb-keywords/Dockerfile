FROM node:argon  
  
ENV DEBUG precon:*  
  
# Create app directory  
RUN mkdir -p /usr/src/precon/message-processors/imdb-keywords  
WORKDIR /usr/src/precon/message-processors/imdb-keywords  
  
# Install app dependencies  
COPY package.json /usr/src/precon/message-processors/imdb-keywords  
  
COPY start.sh /opt  
  
RUN chmod +x /opt/start.sh  
  
RUN npm install  
  
RUN apt-get update  
  
RUN apt install vim -y  
  
# Bundle app source  
COPY . /usr/src/precon/message-processors/imdb-keywords  
  
#RUN node runner.js &> /usr/src/precon/message-processors/imdb-
keywords/dockerlogs  
CMD ["/usr/local/bin/node", "/usr/src/precon/message-processors/imdb-
keywords/runner.js"]  
#ENTRYPOINT ["/usr/local/bin/node", "/usr/src/precon/message-processors/imdb-
keywords/runner.js"]  
#ENTRYPOINT node runner.js

