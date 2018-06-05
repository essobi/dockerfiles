FROM ubuntu:17.10  
MAINTAINER filippocucchetto@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y build-essential wget git cmake xvfb lcov ruby
qt5-default qtdeclarative5-dev qtdeclarative5-private-dev
qtdeclarative5-qtquick2-plugin qtquickcontrols2-5-dev  
RUN gem install coveralls-lcov  
  
COPY build.sh /root  

