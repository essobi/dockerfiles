FROM tragus/ubuntu  
  
MAINTAINER James Johnson  
  
RUN apt-get update && \  
apt-get -y install rsyslog postfix bsd-mailx mailutils  
  
# Perform build-time configuration of the container  
ADD postfix.configure /usr/local/bin/postfix.configure  
RUN chmod +x /usr/local/bin/postfix.configure  
RUN /usr/local/bin/postfix.configure  
  
# Install any other scripts  
ADD postfix.start /usr/local/lib/container-controller/start/  
ADD postfix.stop /usr/local/lib/container-controller/stop/  
  
ENTRYPOINT ["/usr/local/bin/container-controller.start"]  

