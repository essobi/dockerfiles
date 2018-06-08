FROM octasic/base_jenkins_slave  
  
LABEL Description="Jenkins slave for armhf builds"  
  
USER root  
  
RUN apt-get -y update && \  
apt-get install -y g++-arm-linux-gnueabihf && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER jenkins  

