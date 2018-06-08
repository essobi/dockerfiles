FROM centos:centos7  
  
MAINTAINER Dmitry Orlov <me@mosquito.su>  
  
RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum localinstall -y
http://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-
release-1.0-13.ius.centos7.noarch.rpm  
RUN yum localinstall -y
http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-1.noarch.rpm  
RUN yum install -y http://nginx.org/packages/centos/7/noarch/RPMS/nginx-
release-centos-7-0.el7.ngx.noarch.rpm  
  
RUN yum upgrade -y  
  
RUN yum groupinstall -y 'Development Tools'  
RUN yum install -y zlib-devel python-devel libxslt-devel wget \  
libxml2-devel libyaml-devel libpng-devel libjpeg-devel python-pip  
  
RUN mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled
/etc/nginx/conf.d  
  
RUN pip install j2cli  
  
# install grafana  
RUN yum install -y
https://grafanarel.s3.amazonaws.com/builds/grafana-2.0.2-1.x86_64.rpm  
  
ENV ADMIN_USER=admin \  
ADMIN_PASSWORD=admin \  
ADMIN_EMAIL=admin@example.net \  
SECRET_KEY=MY_SUPER_SECRET \  
ALLOW_SIGNUP=true \  
ORGANIZATION_NAME="Eample Inc."  
# add templates  
RUN mkdir -p /etc/templates  
COPY configs/grafana.ini /etc/templates/grafana.j2  
  
# start.sh  
COPY configs/start.sh /usr/local/bin/start.sh  
RUN chmod a+x /usr/local/bin/start.sh  
  
# defaults  
EXPOSE 80:80  
VOLUME [ "/var/lib/grafana" ]  
  
CMD ["/usr/local/bin/start.sh"]  

