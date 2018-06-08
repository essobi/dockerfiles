# docker build -t keystone-mitaka .  
FROM centos:7  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
  
RUN yum -y update && \  
yum -y install epel-release centos-release-openstack-mitaka  
  
RUN yum -y update && \  
yum -y install \  
bind-utils \  
chrony \  
git \  
httpd \  
mariadb \  
mod_ssl \  
mod_wsgi \  
openstack-dashboard \  
openstack-keystone \  
python-openstackclient \  
wget  
  
RUN yum -y install
https://github.com/pingidentity/mod_auth_openidc/releases/download/v2.1.0/cjose-0.4.1-1.el7.centos.x86_64.rpm  
RUN yum -y install
https://github.com/pingidentity/mod_auth_openidc/releases/download/v2.1.2/mod_auth_openidc-2.1.2-1.el7.centos.x86_64.rpm  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod -v +x /entrypoint.sh  
EXPOSE 80 5000 35357  
CMD ["/entrypoint.sh"]  

