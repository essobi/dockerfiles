From ubuntu:trusty  
MAINTAINER Lukas Hetzenecker  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
RUN apt-get update  
  
# Install  
RUN apt-get -y install supervisor  
RUN apt-get -y install dovecot-core dovecot-imapd dovecot-lmtpd dovecot-
managesieved dovecot-sieve dovecot-ldap  
RUN rm -rf /etc/dovecot/*conf*  
RUN touch /etc/dovecot/dovecot.conf  
  
# Add files  
ADD assets/install.sh /opt/install.sh  
  
# Run  
CMD /opt/install.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf  
  

