FROM matwey/opensuse-go  
MAINTAINER Matwey V. Kornilov <matwey.kornilov@gmail.com>  
  
COPY ./run.sh /  
RUN mkdir /data  
  
VOLUME ["/data"]  
ENTRYPOINT ["/run.sh"]  

