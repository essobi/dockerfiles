FROM ubuntu:latest  
MAINTAINER Nikolay Sokolov <nsokolov@qubell.com>  
  
RUN apt-get update && apt-get install -y socat  
ADD run.sh /run.sh  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/run.sh"]  
CMD []  

