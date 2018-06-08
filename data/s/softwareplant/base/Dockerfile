FROM centos:7  
USER root  
  
RUN mkdir -p /preconfig /opt/phantomjs  
  
ADD
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
/preconfig/phantomjs.tar.bz2  
  
ADD elastic.repo /etc/yum.repos.d/  
RUN rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch  
#ADD filebeat.yml /etc/filebeat/  
#ADD metricbeat.yml /etc/metricbeat/  
RUN yum -y update \  
&& yum -y install \  
bzip2 \  
dejavu*fonts \  
filebeat \  
metricbeat \  
fontconfig \  
gettext \  
gnu*fonts \  
less \  
nano \  
tail \  
tree \  
vim \  
wget \  
which \  
unzip \  
telnet \  
&& yum -y clean all  
  
RUN tar xf /preconfig/phantomjs.tar.bz2 -C /opt/phantomjs --strip-components=1
&& rm -rf /preconfig/phantomjs.tar.bz2  
RUN ln -s /opt/phantomjs/bin/phantomjs /bin/phantomjs  
RUN ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime  

