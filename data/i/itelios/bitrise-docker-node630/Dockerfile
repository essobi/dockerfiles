FROM bitriseio/docker-bitrise-base:latest  
  
MAINTAINER Vincent Saluzzo <vincent.saluzzo@itelios.com>  
  
LABEL Description="This image was provided by itelios to Bitrise user who want
a NodeJS 4 LTS context in builds (no Android SDK here)"  
  
RUN cd ~ && wget https://nodejs.org/dist/v6.3.0/node-v6.3.0-linux-x64.tar.xz  
RUN cd ~ && tar --strip-components 1 -xf node-v6.3.0-linux-x64.tar.xz -C
/usr/local  
  
RUN apt-get update && apt-get install -y zip  
  
CMD node -v  

