FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
MAINTAINER Galex Yen "galex@remitly.com"  
# Make bash default shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
575159689BEFB442  
RUN echo 'deb http://download.fpcomplete.com/ubuntu trusty main'| tee
/etc/apt/sources.list.d/fpco.list  
  
RUN apt-get -y update  
RUN apt-get install -y stack  
  
RUN apt-get install -y nodejs  
RUN apt-get install -y npm  
RUN npm install -g less  
RUN npm install -g less-plugin-clean-css  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN stack setup --resolver lts-5.18  
RUN stack install --resolver lts-5.18 hakyll-4.7.5.1  
  
RUN $HOME/.local/bin/hakyll-init build-site  
WORKDIR /build-site  
RUN stack init --verbose  
RUN stack build  
WORKDIR /  
RUN rm -rf build-site  

