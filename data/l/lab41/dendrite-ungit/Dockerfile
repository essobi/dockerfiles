FROM lab41/dendrite-repos  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
# ungit  
RUN sed "s|allowedDomains: 'http://localhost:8000',|allowedDomains: '*',|" -i
/Dendrite/src/main/nodejs/ungit/source/config.js  
RUN npm install -g grunt-cli coffee-script through2  
  
WORKDIR /Dendrite/src/main/nodejs/ungit  
RUN git submodule update --init  
RUN rm -rf node_modules  
RUN npm cache clean  
RUN npm update  
RUN npm install --loglevel info  
RUN grunt --force  
  
ADD npm.conf /etc/supervisor/conf.d/npm.conf  

