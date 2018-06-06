FROM fedora  
  
MAINTAINER rmcook84@gmail.com  
  
# Install the necessary software for our example  
RUN dnf -y install etcd httpd && dnf clean all  
  
# Download confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 -o confd && mv confd /usr/sbin/confd && chmod +x /usr/sbin/confd  
  
# Add our confd configuration directory  
ADD confd /etc/confd  
  
# Our start-up file  
ADD startup.sh /opt/  
  
# Our startup command  
CMD ["/bin/bash", "/opt/startup.sh"]  

