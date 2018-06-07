FROM centos:7  
MAINTAINER Fer Uria <fauria@gmail.com>  
  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum repolist  
RUN yum install -y certbot  
  
VOLUME /web  
VOLUME /etc/letsencrypt/archive  
  
ENTRYPOINT ["certbot", "certonly", "-n", "--agree-tos", "--webroot", "--
webroot-path", "/web", "-d"]

