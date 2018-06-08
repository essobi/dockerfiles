FROM dockerage/apache:latest  
MAINTAINER Xu Wang <xuwang@gmail.com>  
  
ENV DEBIAN_PRIORITY=critical  
# Install base packages  
RUN apt-get update && apt-get -y install \  
pkg-config \  
libcurl3 \  
liblasso3  
  
# Install mod-auth-mellon 0.10.0, the deb is create by apache-mellon-builder  
ADD ./libapache2-mod-auth-mellon_0.10.0-1_amd64.deb /tmp/libapache2-mod-auth-
mellon_0.10.0-1_amd64.deb  
RUN dpkg -i /tmp/libapache2-mod-auth-mellon_0.10.0-1_amd64.deb  
# && rm /tmp/libapache2-mod-auth-mellon_0.10.0-1_amd64.deb  
# Activate mod_proxy  
RUN a2enmod \  
rewrite \  
headers \  
proxy \  
proxy_http \  
proxy_wstunnel  
  
ADD ./mellon /etc/apache2/mellon  
ADD ./ssl /etc/apache2/ssl  

