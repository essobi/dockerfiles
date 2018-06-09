FROM tragus/ubuntu  
  
MAINTAINER James Johnson  
  
RUN apt-get update && \  
apt-get -y install apache2  
  
# Perform build-time configuration of the container  
ADD apache2.configure /usr/local/bin/apache2.configure  
RUN chmod +x /usr/local/bin/apache2.configure &&
/usr/local/bin/apache2.configure  
  
# Install any other scripts  
ADD apache2.start /usr/local/lib/container-controller/start/  
ADD apache2.stop /usr/local/lib/container-controller/stop/  
  
ENTRYPOINT ["/usr/local/bin/container-controller.start"]  

