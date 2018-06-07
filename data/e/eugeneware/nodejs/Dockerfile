# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Eugene Ware <eugene@noblesamurai.com>  
  
RUN apt-get update  
  
# To get add-apt-repository  
RUN apt-get install -y software-properties-common python-software-properties  
  
# Install Node.js  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
  
# For building native modules  
RUN apt-get install -y build-essential openssl libssl-dev pkg-config  
  
# For phantomjs binaries  
RUN apt-get install -y libfreetype6 libfontconfig  
  
# Add some helper command line things  
RUN npm install -g yo serve generator-nodejs  
  
# Append to $PATH variable.  
RUN echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >>
/root/.profile  
  
WORKDIR /data  
ENV HOME /root  
  
# Define default command.  
CMD ["node"]  

