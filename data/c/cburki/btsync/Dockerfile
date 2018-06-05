FROM debian:jessie  
MAINTAINER Christophe Burki, christophe@burkionline.net  
  
# Install system requirements  
RUN apt-get update && apt-get install -y \  
locales  
  
# Configure locales and timezone  
RUN locale-gen en_US.UTF-8  
RUN locale-gen en_GB.UTF-8  
RUN locale-gen fr_CH.UTF-8  
RUN cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime  
RUN echo "Europe/Zurich" > /etc/timezone  
  
# Install btsync  
ADD http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable
/tmp/btsync.tar.gz  
RUN tar zxvf /tmp/btsync.tar.gz -C /usr/bin/ btsync  
  
# s6 install and config  
COPY bin/* /usr/bin/  
COPY configs/etc/s6 /etc/s6/  
  
# btsync config  
COPY configs/etc/btsync.conf /etc/btsync.conf  
  
EXPOSE 55555  
CMD ["/usr/bin/s6-svscan", "/etc/s6"]  

