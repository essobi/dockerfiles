FROM ubuntu:13.10  
MAINTAINER Tim Sogard <docker@timsogard.com>  
  
ADD cfg /opt/wsw_cfg/  
RUN apt-get update  
RUN apt-get install wget libcurl3 libcurl3-gnutls -y  
  
# Install game from warsow.net  
RUN wget --no-verbose -O warsow_1.02_unified.tar.gz
http://www.warsow.net/download?dl=linux102  
RUN tar zxf warsow_1.02_unified.tar.gz -C /opt/  
RUN chmod +x /opt/warsow_1.02/wsw_server*  
  
# Setup user  
RUN useradd -m -s /bin/bash warsow  
RUN chown -R warsow:warsow /opt/warsow_1.02  
  
# Setup server  
WORKDIR /opt/warsow_1.02  
USER warsow  
EXPOSE 44401/udp  
  
CMD ./wsw_server +set fs_usehomedir 0 +set fs_basepath /opt/warsow_1.02/ +set
dedicated 1  

