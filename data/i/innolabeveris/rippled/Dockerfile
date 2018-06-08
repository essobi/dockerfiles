FROM ubuntu:16.04  
#TODO FROM phusion/baseimage  
RUN apt-get -y update  
RUN apt-get -y install yum-utils alien  
RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm  
RUN yumdownloader --enablerepo=ripple-stable --releasever=el7 rippled  
RUN rpm --import https://mirrors.ripple.com/rpm/RPM-GPG-KEY-ripple-release &&
rpm -K rippled*.rpm  
RUN alien -i --scripts rippled*.rpm && rm rippled*.rpm  
  
# peer_port  
EXPOSE 51235  
# websocket_public_port  
EXPOSE 5006  
# websocket_port (trusted access)  
EXPOSE 6006  
# Share the ripple data directory  
VOLUME /var/lib/rippled  
  
# Add custom config  
ADD rippled.conf /opt/ripple/etc/rippled.conf  
  
CMD ["/opt/ripple/bin/rippled", "--conf", "/opt/ripple/etc/rippled.conf"]  

