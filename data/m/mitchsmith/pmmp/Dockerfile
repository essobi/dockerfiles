FROM php:7.2-rc  
  
RUN apt-get -y update  
RUN apt-get -y install wget  
  
RUN mkdir /opt/pmmp  
RUN useradd -r docker  
RUN chown -R docker:docker /opt/pmmp  
  
USER docker:docker  
  
RUN cd /opt/pmmp && wget -q -O - https://get.pmmp.io | bash -s - -r  

