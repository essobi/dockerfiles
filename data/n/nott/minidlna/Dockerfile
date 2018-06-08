FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum localinstall --nogpgcheck
http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E
%fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-
nonfree-release-$(rpm -E %fedora).noarch.rpm --assumeyes  
RUN yum -y update; yum clean all;  
RUN yum -y install minidlna  
  
ADD minidlna.conf /etc/minidlna.conf  
RUN chown minidlna: /etc/minidlna.conf  
  
VOLUME ["/data"]  
  
EXPOSE 1900/udp  
EXPOSE 8200  
CMD /usr/sbin/minidlnad -d -f /etc/minidlna.conf  

