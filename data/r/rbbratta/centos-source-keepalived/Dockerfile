FROM rbbratta/centos-source-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN yum -y install hostname keepalived socat && yum clean all  
  
COPY check_alive.sh /  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start /check_alive.sh  
  

