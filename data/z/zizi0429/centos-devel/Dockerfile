FROM centos:6  
  
RUN yum update -y \  
&& yum -y install yum-plugin-fastestmirror \  
&& yum -y install epel-release \  
&& yum -y localinstall "https://centos6.iuscommunity.org/ius-release.rpm" \  
&& yum -y localinstall "http://packages.groonga.org/centos/groonga-
release-1.1.0-1.noarch.rpm" \  
&& yum -y install \  
sudo \  
tar \  
wget \  
&& yum -y groupinstall "Development Tools" \  
&& yum clean all \  
&& echo "include_only=.jp" >> /etc/yum/pluginconf.d/fastestmirror.conf \  
&& sed -i -e "s/enabled *= *1/enabled=0/g" /etc/yum.repos.d/epel.repo \  
&& sed -i -e "s/enabled *= *1/enabled=0/g" /etc/yum.repos.d/ius.repo \  
&& sed -i -e "s/enabled *= *1/enabled=0/g" /etc/yum.repos.d/groonga.repo \  
&& localedef -f UTF-8 -i ja_JP /usr/lib/locale/ja_JP.UTF-8  
ENV TERM xterm-256color  
  
RUN mkdir /home/workspace  
WORKDIR /home/workspace  

