FROM node:4.4  
RUN mkdir /opt/app  
# use changes to package.json to force Docker not to use the cache  
# when we change our application's nodejs dependencies:  
COPY package.json /tmp/package.json  
COPY bower.json /tmp/bower.json  
RUN cd /tmp && npm install -g bower grunt-cli http-server && npm install &&
bower --allow-root install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/ && cp -a
/tmp/bower_components /opt/app/  
  
# From here we load our application's code in, therefore the previous docker  
# "layer" thats been cached will be used if possible  
WORKDIR /opt/app  
COPY . /opt/app  
RUN grunt build  
CMD ["http-server", "/opt/app/dist", "-d", "False"]  

