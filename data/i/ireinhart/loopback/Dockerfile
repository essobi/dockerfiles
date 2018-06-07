FROM ireinhart/node-dev  
MAINTAINER Ingo Reinhart <ingo.reinhart@gmail.com>  
ADD . /install  
WORKDIR /install  
RUN npm install -g $(cat packages) && rm -rf npm_cache /tmp/*  
ENV NODE_PATH /usr/local/lib/node_modules/  

