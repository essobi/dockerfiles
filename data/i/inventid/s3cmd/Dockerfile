FROM alpine:3.1  
MAINTAINER Rogier Slag <rogier@inventid.nl>  
  
VOLUME ["/s3"]  
  
ADD s3cfg /opt/s3cfg  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
ADD run.sh /opt  
RUN chmod 0755 /opt/run.sh  
  
WORKDIR /s3  
  
ENTRYPOINT ["/opt/run.sh"]  

