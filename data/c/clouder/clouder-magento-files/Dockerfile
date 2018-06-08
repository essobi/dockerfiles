FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
# Prepare system  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -qq
install wget  
# Download and unpack Magento  
RUN cd /tmp && wget https://github.com/OpenMage/magento-
mirror/archive/magento-1.9.tar.gz  
RUN cd /tmp && tar -zxvf magento-1.9.tar.gz  
RUN mkdir -p /opt/magento  
RUN mv /tmp/magento-mirror-magento-1.9 /opt/magento/files  
RUN cd /tmp && rm -f magento-*tar.gz  

