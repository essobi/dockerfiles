From ubuntu:trusty  
MAINTAINER Elliott Ye  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
RUN apt-get update  
  
# Start editing  
# Install package here for cache  
RUN apt-get -y install supervisor postfix sasl2-bin opendkim opendkim-tools
courier-imap mailutils  
  
# Add files  
ADD assets/install.sh /opt/install.sh  
  
EXPOSE 143  
EXPOSE 25  
# Run  
CMD /opt/install.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

