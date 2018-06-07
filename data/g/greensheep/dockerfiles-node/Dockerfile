FROM node:0.10.33  
MAINTAINER Tom Hill <tom@greensheep.io>  
  
# Install NPM packages  
RUN npm install -g grunt-cli bower mocha  
  
# Install ruby / sass  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y install ruby \  
&& gem install sass  
  
# Create app folder  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/app"]  
  
EXPOSE 8888  
CMD ["/bin/bash"]  

