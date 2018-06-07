# version 1.0.0  
FROM ubuntu:14.04  
MAINTAINER Dean Huakau "deanhuakau@hotmail.co.nz"  
RUN apt-get -yqq update  
  
COPY index.html /var/www/html/index.html  
  
VOLUME ["var/www/html"]  
  
ENTRYPOINT [ "/bin/sh", "-c", "while true; do echo im deans datacontainer ;
sleep 60; done" ]  
  

