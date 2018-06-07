# graphite feeder  
#  
# VERSION 1.0.0  
FROM node:latest  
MAINTAINER Sven Müller <sven.mueller@commercetools.de>  
  
# clone repo  
RUN git clone https://github.com/commercetools/graphite-feeder.git /graphite-
feeder  
  
# install grunt  
RUN npm install -g grunt-cli  
  
#resolve dependencies and build application  
RUN cd graphite-feeder && npm install && grunt  
  
ENTRYPOINT ["/graphite-feeder/bin/feeder"]  

