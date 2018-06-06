FROM rbbratta/centos-source-ceilometer-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi gettext && yum clean all  
  
RUN sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
COPY extend_start.sh /usr/local/bin/kolla_ceilometer_extend_start  
RUN chmod 755 /usr/local/bin/kolla_ceilometer_extend_start  
  

