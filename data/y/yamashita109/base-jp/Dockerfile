FROM centos:7.2.1511  
MAINTAINER yamashita109  
  
ENV TERM xterm  
  
# Make Japanese locale files  
RUN /usr/bin/localedef -f UTF-8 -i ja_JP /usr/lib/locale/ja_JP.UTF-8  
ENV LC_ALL=ja_JP.UTF-8  
# Set timezone  
# To use timedatectl is a proper way but it bring about  
# bus connection error of lacking needed privilege.  
# In addition, docker cannot use --privileged option while building,  
# therefore it copy timezone information manually.  
RUN rm /etc/localtime; ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime;  
  
RUN yum -y update \  
&& yum install -y \  
vim \  
tree \  
curl \  
wget \  
ctags \  
git \  
&& yum clean all \  
&& rm -rf /var/cache/yum/*  
  
# The container is started with traditional init process.  
CMD /sbin/init  

