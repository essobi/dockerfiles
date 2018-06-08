From ubuntu:trusty  
MAINTAINER Christoph Dwertmann  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update -qq && \  
apt-get -y install supervisor postfix sasl2-bin opendkim opendkim-tools curl
busybox pcregrep && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# Add files  
ADD assets/*.sh /opt/  
  
# Run  
CMD /opt/install.sh;/usr/bin/supervisord -c
/etc/supervisor/supervisord.conf;busybox tail -F /var/log/mail.log

