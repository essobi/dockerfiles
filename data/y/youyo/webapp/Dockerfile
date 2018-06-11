FROM centos:centos7  
MAINTAINER youyo  
  
ENV CONSUL_VERSION 0.6.4  
RUN yum install -y \  
epel-release \  
http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm epel-release && \  
yum install -y \  
nginx \  
wget \  
unzip \  
supervisor && \  
wget
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&& \  
unzip consul_${CONSUL_VERSION}_linux_amd64.zip -d /usr/local/sbin/ && \  
chmod 700 /usr/local/sbin/consul && \  
mkdir /etc/consul.d && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY consul.json /etc/consul.d/consul.json  
COPY index.shtml /usr/share/nginx/html/index.shtml  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

