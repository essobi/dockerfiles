FROM fedora:23  
MAINTAINER Tavis Aitken <tavisto@tavisto.net>  
  
RUN /usr/bin/dnf -y -q update && dnf -y install rpmdevtools mock rpmlint git
wget curl  
RUN adduser rpmbuilder && usermod rpmbuilder -aG mock  
RUN su rpmbuilder -c rpmdev-setuptree

