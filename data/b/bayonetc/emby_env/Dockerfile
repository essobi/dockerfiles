FROM centos/systemd  
  
MAINTAINER Jerend Cao "bayonet_c@163.com"  
RUN yum -y install -y epel-release wget \  
&& wget
https://download.opensuse.org/repositories/home:emby/CentOS_7/home:emby.repo \  
&& mv home:emby.repo /etc/yum.repos.d \  
&& yum install -y emby-server \  
&& rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-1.el7.nux.noarch.rpm \  
&& yum install -y ffmpeg \  
&& yum clean all \  
&& systemctl enable emby-server  
  
VOLUME ["/library"]  
EXPOSE 8096 8920 7359/udp 1900/udp  
  
CMD ["/usr/sbin/init"]  
  

