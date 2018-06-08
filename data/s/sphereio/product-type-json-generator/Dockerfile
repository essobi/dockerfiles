# product type generator  
#  
# VERSION 1.0.0  
FROM node:latest  
MAINTAINER Sven Müller <sven.mueller@commercetools.de>  
  
# clone repo  
RUN git clone https://github.com/sphereio/sphere-product-type-json-
generator.git /json-generator  
  
# install grunt  
RUN npm install -g grunt-cli  
  
#resolve dependencies and build application  
RUN cd /json-generator && npm install && grunt build  
  
ENTRYPOINT ["/json-generator/bin/product-type-json-generator"]  

