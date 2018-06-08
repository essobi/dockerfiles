## -*- docker-image-name: "rezarahimi/debian-fusiondirectory" -*-  
FROM rezarahimi/debian-php  
MAINTAINER Reza Rahimi <rezarahimi@gmail.com>  
  
ENV FUSIONDIRECTORY_VERSION 1.0.8.2  
ENV FUSIONDIRECTORY_DEB_PKG_VERSION 1.0.8.2-5+deb8u1  
  
RUN apt-get update && \  
apt-get install -y argonaut-server
fusiondirectory=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-mail=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-systems=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ldapdump=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-ldapmanager=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-weblink=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-plugin-webservice=${FUSIONDIRECTORY_DEB_PKG_VERSION} \  
fusiondirectory-webservice-shell=${FUSIONDIRECTORY_DEB_PKG_VERSION}  

