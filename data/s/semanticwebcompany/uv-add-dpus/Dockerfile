FROM alpine:3.3  
MAINTAINER Niels Vandekeybus <niels.vandekeybus@tenforce.com>  
ADD dpus /dpus  
VOLUME /dpus  
ENV MASTER_USER=master MASTER_PASSWORD=commander FRONTEND=frontend
FRONTENDPORT=8088  
RUN apk add --no-cache bash curl  
RUN mkdir -p /var/log/adddpus  
RUN chmod 777 /var/log/adddpus  
ADD download.sh /dpus/download.sh  
RUN chmod +x /dpus/download.sh && ./dpus/download.sh  
ADD startup.sh add-dpu.sh /usr/local/bin/  
CMD ["/bin/bash", "/usr/local/bin/startup.sh"]  
  

