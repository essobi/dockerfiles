FROM centos:7  
MAINTAINER sohrkim@gmail.com  
  
RUN yum localinstall -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& yum localinstall -y
https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-
installer-2.6-1.noarch.rpm \  
&& yum install -y xorg-x11-font-utils fontconfig fonttools nhn-nanum-gothic-
fonts google-noto-sans*-fonts  
  
COPY wkhtmltox-0.12.2.1_linux-centos7-amd64.rpm /tmp/  
RUN yum localinstall -y /tmp/wkhtmltox-0.12.2.1_linux-centos7-amd64.rpm && rm
-f /tmp/wkhtmltox-0.12.2.1_linux-centos7-amd64.rpm  
  

