# Copyright (C) 2015 Bitergia  
# GPLv3 License  
  
FROM tomcat:7.0  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# download and install Authzforce (service starts Automatically)  
  
RUN curl -O -L
http://catalogue.fiware.org/sites/default/files/storage/enablers/authzforce_4.2.0-fiware_all.deb
&& \  
dpkg --extract authzforce_4.2.0-fiware_all.deb /root/authzforce/ && \  
mv /root/authzforce/etc/tomcat7/Catalina /usr/local/tomcat/conf/ && \  
mv /root/authzforce/opt/* /opt/ && \  
rm -rf /opt/authzforce/data/domains/* && \  
rm -rf /root/authzforce && \  
rm -f authzforce_4.2.0-fiware_all.deb  
  
### Exposed ports  
# - App server  
EXPOSE 8080  

