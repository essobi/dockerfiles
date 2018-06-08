From ubuntu:trusty  
MAINTAINER info@pojo-ict.nl  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
# Start editing  
# Install package here for cache  
RUN apt-get update > /dev/null && \  
apt-get -y install supervisor postfix sasl2-bin opendkim opendkim-tools
mailutils > /dev/null && \  
apt-get clean > /dev/null  
# Add files  
ADD assets/install.sh /opt/install.sh  
  
EXPOSE 25  
# Run  
CMD /opt/install.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf  
  

