FROM fbarth/dockerbase-node:8.4.0  
RUN echo deb http://archive.ubuntu.com/ubuntu trusty main universe >
/etc/apt/sources.list  
RUN echo deb http://archive.ubuntu.com/ubuntu trusty-updates main universe >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y ghostscript  
RUN apt-get install -y pdftk  
RUN apt-get install -y imagemagick  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

