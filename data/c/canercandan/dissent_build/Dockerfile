FROM ubuntu:14.04  
MAINTAINER Caner Candan <caner@candan.fr>  
  
RUN apt-get -qq update && apt-get -qqy install git build-essential doxygen
qt5-default libcrypto++-dev gdb  
  
WORKDIR /tmp/dissent  
  
RUN git clone https://github.com/DeDiS/Dissent.git .  
  
WORKDIR /tmp/dissent/build  
  
RUN doxygen ../dissent.doxy  
RUN qmake ../application.pro && make  
  
VOLUME /dissent  
  
CMD {\  
mv /tmp/dissent/build/dissent /dissent/ && \  
mv /tmp/dissent/build/docs /dissent/; \  
}  

