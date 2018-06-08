FROM ubuntu  
MAINTAINER Kyle Harding <kylemharding@gmail.com>  
  
RUN apt-get update && \  
apt-get install megatools -y  
  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
COPY ./run.sh /root/  
COPY ./sample.conf /root/  
  
RUN chmod +x /root/run.sh  
  
VOLUME /config /uploads  
  
ENTRYPOINT ["/root/run.sh"]  

