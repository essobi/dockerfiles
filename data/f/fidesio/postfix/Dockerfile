FROM fidesio/ubuntu:trusty  
# Maintainer  
MAINTAINER Fidesio <docker@fidesio.com>  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
RUN apt-get update  
  
# Start editing  
# Install package here for cache  
RUN apt-get -y install supervisor postfix sasl2-bin opendkim opendkim-tools  
  
# Add files  
ADD scripts/install.sh /opt/install.sh  
  
# Run  
CMD /bin/bash /opt/install.sh;/usr/bin/supervisord -c
/etc/supervisor/supervisord.conf

