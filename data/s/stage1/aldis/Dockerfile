FROM debian:latest  
  
MAINTAINER Geoffrey Bachelet <geoffrey@stage1.io>  
  
RUN echo deb http://http.debian.net/debian wheezy-backports main >>
/etc/apt/sources.list  
RUN apt-get update -y  
RUN apt-get install -y nodejs nodejs-legacy curl git  
RUN curl https://www.npmjs.org/install.sh | clean=no sh  
RUN npm install -g coffee-script  
  
RUN git clone https://github.com/stage1/aldis.git /aldis  
  
WORKDIR /aldis  
RUN npm install  
  
ENTRYPOINT ["/usr/bin/coffee", "/aldis/aldis.coffee"]

