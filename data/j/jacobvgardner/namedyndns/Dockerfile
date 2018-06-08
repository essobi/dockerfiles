FROM mhart/alpine-node:latest  
  
MAINTAINER Jacob Gardner <jacob.v.gardner@gmail.com>  
  
RUN ["mkdir", "-p", "/opt/namedyndns"]  
WORKDIR /opt/namedyndns  
ADD package.json /opt/namedyndns  
RUN ["npm", "install"]  
  
ADD .babelrc /opt/namedyndns  
ADD main.js /opt/namedyndns  
  
RUN ["npm", "run", "build"]  
  
ENTRYPOINT ["node", "dist/main.js"]

