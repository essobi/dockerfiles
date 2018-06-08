FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum localinstall --nogpgcheck
http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E
%fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-
nonfree-release-$(rpm -E %fedora).noarch.rpm --assumeyes  
RUN yum -y update; yum clean all;  
RUN yum -y install ffmpeg  
  
ENTRYPOINT ["/usr/bin/ffmpeg"]

