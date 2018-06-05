# alexindigo/node-dev  
FROM alexindigo/base-dev:ubuntu_12.04-1  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
# Pull latest node  
RUN curl -s -L http://nodejs.org/dist/node-latest.tar.gz -o node-latest.tar.gz
&& tar -xzf node-latest.tar.gz  
  
# Install node  
RUN cd "$(ls | grep node-v)" && ./configure && make && make install  
  
# Cleanup  
RUN rm -rf node-*  

