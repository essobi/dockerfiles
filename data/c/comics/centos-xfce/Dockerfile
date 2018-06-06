FROM centos:latest  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: -  
# Software Version: -  
# Software Website: -  
# Description: Base Centos7 with XFCE Desktop and VNC  
##############################################################  
  
ENV DISPLAY=:1 \  
VNC_PORT=5901  
  
EXPOSE $VNC_PORT  
  
ENV HOME=/comics \  
VNC_RES=1280x1024 \  
VNC_COL_DEPTH=24 \  
VNC_PSSWRD=myvncpassword \  
VNC_VIEWONLY=false  
WORKDIR $HOME  
  
RUN yum update -y ; \  
yum install -y epel-release ; \  
yum install -y ansible \  
git \  
gcc \  
gcc-c++ \  
gettext \  
make \  
net-tools \  
nss_wrapper \  
sudo \  
tigervnc-server-minimal \  
x11vnc \  
xinetd \  
which ; \  
yum groups install -y Xfce ; \  
yum -y groups install "Fonts" ; \  
yum erase -y *power* *screensaver* ; \  
rm /etc/xdg/autostart/xfce-polkit* ; \  
/bin/dbus-uuidgen > /etc/machine-id ; \  
yum update -y ; \  
yum clean all ; \  
curl -o /usr/local/sbin/gosu -L
https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64 ; \  
chmod 0755 /usr/local/sbin/gosu ;  
  
  
COPY user_entrypoint.sh /usr/local/bin/user_entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/user_entrypoint.sh"]  

