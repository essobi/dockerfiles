# USAGE:  
#  
#PULL the image:  
#  
#  
# docker run --rm -p 10010:10010 -v /home/olivier:/home/userxpra -u 1000:1000
olivierpt/emacs-xpra  
#  
# BASE IMAGE: Centos LSB  
FROM centos:latest  
  
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
xorg-x11-server-Xvfb \  
emacs  
  
RUN dbus-uuidgen > /etc/machine-id  
  
# expose HTML5 port (experimental)  
EXPOSE 8080  
# expose raw TCP port  
EXPOSE 10010  
CMD ["xpra", "start", ":10", "--start-child=emacs", "--daemon=off", "--bind-
tcp=0.0.0.0:10010"]  

