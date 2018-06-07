###### Updated version of fedora (24)  
FROM fedora:24  
MAINTAINER "Christian Kniep <christian@qnib.org>"  
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
  
ADD etc/yum.conf /etc/yum.conf  
RUN dnf install -y python-dnf-plugins-extras-migrate \  
&& dnf-2 migrate \  
&& dnf clean all \  
&& dnf update -y -x systemd -x systemd-libs -x iputils \  
&& dnf install -y wget vim curl hostname iproute  

