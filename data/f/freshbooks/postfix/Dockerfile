From ubuntu:trusty  
MAINTAINER Elliott Ye  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Start editing  
# Install package here for cache  
RUN apt-get -y install supervisor postfix-pcre sasl2-bin opendkim opendkim-
tools  
  
# Add files  
ADD assets/install.sh /opt/install.sh  
  
# Run  
CMD /opt/install.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

