FROM ubuntu:16.04  
MAINTAINER filippocucchetto@gmail.com  
  
RUN apt-get update && apt-get install -y build-essential wget git cmake xvfb
lcov ruby qt5-default qtdeclarative5-dev qtdeclarative5-private-dev
qtdeclarative5-qtquick2-plugin qtdeclarative5-controls-plugin  
RUN gem install coveralls-lcov  

