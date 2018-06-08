# USAGE:  
#  
#PULL the image:  
# docker pull olivierpt/xterm-xpra  
#  
# docker run --rm -p 10010:10010 -v /home:/home \  
# -v /etc/group:/etc/group:ro -v /etc/passwd:/etc/passwd:ro \  
# --privileged -u $( id -u $USER ):$( id -g $USER ) \  
# --device=dev/dri:/dev/dri  
# olivierpt/glxgears-xpra  
#  
FROM centos:7.3.1611  
MAINTAINER olivier.pillaudtirard@gmail.com  
  
RUN yum update -y && \  
yum install -y epel-release curl  
  
RUN yum repolist  
  
RUN cd /etc/yum.repos.d && curl -O
https://winswitch.org/downloads/CentOS/winswitch.repo  
  
RUN yum repolist  
  
RUN yum install -y pangox-compat \  
xpra \  
which \  
xorg-x11-server-Xvfb  
  
RUN yum update -y && \  
yum -y install mesa-libGL mesa-dri-drivers && \  
rm -rf /var/lib/apt/lists/*  
  
RUN yum install -y glx-utils  
  
RUN dbus-uuidgen > /etc/machine-id  
  
# expose HTML5 port (experimental)  
EXPOSE 8090  
# expose raw TCP port  
EXPOSE 10010  
CMD ["xpra", "start", ":100", "--start-child=glxgears", "--daemon=off", "--
bind-tcp=0.0.0.0:10010", "--html=0.0.0.0:8080"]  

