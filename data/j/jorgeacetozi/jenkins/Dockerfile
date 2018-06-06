FROM jenkins/jenkins:2.60.3  
# File Author / Maintainer  
MAINTAINER Jorge Acetozi  
  
# Install plugins  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  

