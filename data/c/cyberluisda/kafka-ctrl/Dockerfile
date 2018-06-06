FROM openshine/kafka:0.11.0.0  
MAINTAINER Luis David Barrios Alfonso (cyberluisda@gmail.com)  
  
ADD files/kafka-ctl.sh /bin/  
RUN chmod a+x /bin/kafka-ctl.sh  
  
#Add dockerize tool  
ENV DOCKERIZE_VERSION v0.5.0  
RUN curl -L
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
| tar -C /usr/local/bin -xzvf -  
  
ENTRYPOINT ["/bin/kafka-ctl.sh"]  
CMD ["--help"]  

