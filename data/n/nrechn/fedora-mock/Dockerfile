FROM fedora  
MAINTAINER https://github.com/nrechn/fedora-mock  
  
RUN dnf makecache \  
&& dnf -y install spectool mock wget createrepo \  
&& dnf clean all \  
&& rm -rf /tmp/*  

