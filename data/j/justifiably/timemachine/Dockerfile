FROM ubuntu:16.04  
MAINTAINER Justifiably <justifiably@ymail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -yqq netatalk  
  
RUN mkdir -p /timemachine && \  
echo '/timemachine "Timemachine Backups" allow:timemachine
options:usedots,upriv,tm' >> /etc/netatalk/AppleVolumes.default && \  
echo '-setuplog "default log_info /var/log/afpd.log"' >>
/etc/netatalk/afpd.conf  
  
# Also do this on the server for convenience  
RUN useradd timemachine -u 820 -r && \  
echo "timemachine:timemachine" | chpasswd && \  
chown timemachine /timemachine  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN touch /var/log/afpd.log  
  
ADD start.sh /start.sh  
  
EXPOSE 548  
VOLUME ["/timemachine"]  
VOLUME ["/etc/netatalk/"]  
  
CMD [ "/bin/bash", "/start.sh" ]  
  

