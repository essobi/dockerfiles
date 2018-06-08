FROM mainlxc/ubuntu  
MAINTAINER Asokani "https://github.com/asokani"  
RUN apt-get update && \  
apt-get -y install postfix mailutils opendkim opendkim-tools  
  
# startup scripts  
RUN mkdir -p /etc/my_init.d  
  
ADD mailserver.sh /etc/my_init.d/mailserver.sh  
  
# postfix  
RUN mkdir /etc/service/postfix  
ADD postfix.sh /etc/service/postfix/run  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

