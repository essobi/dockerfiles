FROM node:9  
  
RUN apt-get update && apt-get install apt-transport-https  
  
RUN yarn global add \  
elm@0.18 \  
http-server \  
json-server \  
js-yaml \  
nsp \  
nsp-preprocessor-yarn \  
standard \  
doctoc  
  
USER node  

