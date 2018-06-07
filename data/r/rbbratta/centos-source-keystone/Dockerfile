FROM rbbratta/centos-source-keystone-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
COPY keystone_bootstrap.sh /usr/local/bin/kolla_keystone_bootstrap  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_keystone_bootstrap  
  

