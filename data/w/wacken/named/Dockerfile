FROM centos:latest  
  
MAINTAINER Roman Pridybailo <roman.pridybailo@kruschecompany.com>  
  
RUN yum install -y epel-release && yum -y update \  
&& yum install -y bind bind-devel bind-libs bind-utils  
  
RUN mkdir -p /var/named/master && mkdir -p /var/log/named \  
&& chown named:named -R /var/log/named  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
EXPOSE 53/udp 53/tcp 953  
ENTRYPOINT ["docker-entrypoint.sh"]

