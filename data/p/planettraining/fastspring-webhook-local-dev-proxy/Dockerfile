FROM ubuntu:15.10  
RUN apt-get update && apt-get install -y curl python build-essential  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
  
COPY app/package.json /tmp/app/package.json  
  
RUN cd /tmp/app && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/app/node_modules /opt/app/  
COPY app /opt/app  
  
EXPOSE 3010  
WORKDIR /opt/app  
CMD node index.js

