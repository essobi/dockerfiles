FROM ubuntu:14.04  
MAINTAINER Thom Nichols "thom@thomnichols.org"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -qq update  
RUN apt-get install -y nodejs npm  
# TODO could uninstall some build dependencies  
# fucking debian installs `node` as `nodejs`  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
ADD . /src  
RUN cd /src && npm install  
RUN npm install forever -g  
  
EXPOSE 443  
WORKDIR /src  
  
CMD ["forever", "app.js"]

