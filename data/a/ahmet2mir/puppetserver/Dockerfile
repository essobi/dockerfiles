FROM debian:wheezy  
MAINTAINER Ahmet Demir <ahmet2mir+github@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV RELEASE wheezy  
ENV SHELL /bin/bash  
  
RUN echo "deb http://ftp.fr.debian.org/debian $RELEASE main contrib non-free"
> /etc/apt/sources.list;\  
echo "deb http://ftp.debian.org/debian/ $RELEASE-updates main contrib non-
free" >> /etc/apt/sources.list;\  
echo "deb http://security.debian.org/ $RELEASE/updates main contrib non-free"
>> /etc/apt/sources.list;\  
apt-get update  
  
RUN apt-get install -y --no-install-recommends wget ca-certificates  
  
RUN wget -q https://apt.puppetlabs.com/puppetlabs-release-wheezy.deb -O
/tmp/puppetlabs.deb;\  
dpkg -i /tmp/puppetlabs.deb;\  
apt-get update  
  
RUN apt-get install -y --no-install-recommends puppetserver  
  
COPY conf/puppet.conf /etc/puppet/puppet.conf  
COPY conf/autosign.conf /etc/puppet/autosign.conf  
  
EXPOSE 8140  
CMD ["/usr/bin/java","-XX:OnOutOfMemoryError='kill -9
%p'","-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=/var/log/puppetserver","-Xms2g","-Xmx2g","-jar","/usr/share/puppetserver/puppet-
server-release.jar","--config","/etc/puppetserver/conf.d","--bootstrap-
config","/etc/puppetserver/bootstrap.cfg"]  
  

