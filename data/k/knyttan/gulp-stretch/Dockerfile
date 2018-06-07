FROM knyttan/base-stretch:latest  
  
ADD nodesource.gpg.key /tmp/nodesource.gpg.key  
RUN apt-key add /tmp/nodesource.gpg.key  
RUN echo 'deb https://deb.nodesource.com/node_8.x stretch main' >
/etc/apt/sources.list.d/nodesource.list  
  
RUN apt-get update && apt-get install -y nodejs  
  
RUN npm install -g gulp  
  
WORKDIR /app  
  
ONBUILD ARG NPM_TOKEN  
ONBUILD ADD ./package.json /app/package.json  
ONBUILD RUN npm config set //registry.npmjs.org/:_authToken=${NPM_TOKEN}  
ONBUILD RUN npm install --quiet  

