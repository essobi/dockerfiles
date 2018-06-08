FROM centos:centos7  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
RUN yum -y update && yum clean all  
RUN yum -y install epel-release && yum clean all  
  
RUN yum -y install supervisor \  
git \  
bind-utils \  
pwgen \  
psmisc \  
net-tools \  
hostname \  
curl \  
curl-devel \  
sqlite \  
libevent \  
gearmand \  
libgearman \  
libgearman-devel && yum clean all  
  
# Configure servicies  
ADD ./start.sh /start.sh  
ADD ./supervisor-gearmand.ini /etc/supervisord.d/gearmand.ini  
  
RUN chmod 755 /start.sh  
  
RUN mkdir -p /var/log/gearmand  
  
VOLUME ["/var/log/gearmand"]  
  
EXPOSE 4730  
CMD ["/bin/bash", "/start.sh"]  
  

