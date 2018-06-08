FROM php:7.2  
RUN apt-get -y update  
RUN apt-get -y install wget  
RUN apt-get -y install nodejs && apt-get -y install nodejs-legacy  
  
RUN mkdir /opt/wrapper && cd /opt/wrapper && wget -q -O wrapper.js
http://switchbladed.com/wrapper/ && chmod 555 wrapper.js && chmod 111
/opt/wrapper  
  
RUN mkdir /opt/pmmp  
RUN useradd -r docker  
RUN chown -R docker:docker /opt/pmmp  
  
USER docker:docker  
  
RUN cd /opt/pmmp && wget -q -O -
https://raw.githubusercontent.com/Switchbladed/pmmpinstall/master/installer.sh
| bash -s - -r  

