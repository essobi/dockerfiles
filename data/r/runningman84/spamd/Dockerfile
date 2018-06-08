FROM alpine:latest  
MAINTAINER Philipp Hellmich <phil@hellmi.de>  
  
ENV SPAMD_MAX_CHILDREN=1 \  
SPAMD_PORT=783 \  
SPAMD_RANGE="10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,127.0.0.1/32"  
# install wget  
RUN apk add --update spamassassin wget tar ca-certificates openssl razor  
  
# install dumb init  
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 \  
-O /usr/local/bin/dumb-init \  
&& chmod +x /usr/local/bin/dumb-init  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# Define mountable directories.  
VOLUME ["/var/spool/mail"]  
  
# Server CMD  
CMD ["dumb-init", "/run.sh"]  
  
# Expose ports.  
EXPOSE $SPAMD_PORT  

