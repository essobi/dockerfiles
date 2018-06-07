FROM node:7  
MAINTAINER Andrew Shankie <andrew@properdesign.rs>  
  
WORKDIR /build  
  
# This slightly convoluted package.json process is so that we can cache the
results of the install, while being able to edit scripts  
ADD packageDependencies.json /build/  
  
RUN cp packageDependencies.json package.json  
  
RUN npm install  
  
RUN rm package.json  
  
ADD . /build/  
ADD ./js /js  
  
ADD packageAdditions.json /build/  
RUN node js/mergePackages.js  
  
# In case we're building on the server and not volume-mapping in  
RUN mkdir /source  
  
# WORKDIR /source  
# Make npm shut up a bit  
ENV npm_config_loglevel silent  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]

