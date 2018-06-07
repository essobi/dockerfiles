FROM node:6-alpine  
  
MAINTAINER Matej Nemcek <ybdaba@gmail.com>  
  
WORKDIR /src  
  
VOLUME ["/data"]  
  
# use changes to package.json to force Docker not to use the cache  
# when we change our application's dependencies:  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm set progress=false && npm i --no-color  
RUN mkdir -p /src && cp -a /tmp/node_modules /src  
  
ADD . /src  
  
ENV BASE_URL='http://127.0.0.1:5080'  
ENV DATA_DIRECTORY='/data'  
ENV REMOTE_REGISTRY='https://registry.npmjs.org'  
ENV REMOTE_REGISTRY_SKIMDB='https://replicate.npmjs.com'  
EXPOSE 5080  
# Good if you want daisy chain your npms  
#EXPOSE 16984  
CMD npm start -- --r $REMOTE_REGISTRY \  
-R $REMOTE_REGISTRY_SKIMDB \  
-d $DATA_DIRECTORY \  
-u $BASE_URL  

