FROM ubuntu:latest  
RUN apt-get update && \  
apt-get --yes install wget && \  
apt-get --yes install build-essential fakeroot devscripts && \  
apt-get --yes install dh-make && \  
apt-get --yes install git && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD create_package.sh /create_package.sh  
RUN chmod +x /create_package.sh  
ENTRYPOINT ["/create_package.sh"]  

