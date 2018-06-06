FROM chinashrimp/centos-openstack-common  
MAINTAINER lyon "ll_nwpu@163.com"  
RUN set -x \  
&& yum install -y httpd mod_wsgi memcached python-memcached openstack-keystone
python-openstackclient  
  
# copy keystone config puppet file  
COPY keystone.pp /root/keystone.pp  
  
# copy sql script  
COPY keystone.sql /root/keystone.sql  
  
# add bootstrap script and make it executable  
COPY bootstrap.sh /etc/bootstrap.sh  
RUN chown root.root /etc/bootstrap.sh && chmod a+x /etc/bootstrap.sh  
ENTRYPOINT ["/etc/bootstrap.sh"]  

