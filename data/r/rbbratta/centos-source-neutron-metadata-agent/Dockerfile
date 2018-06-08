FROM rbbratta/centos-source-neutron-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
COPY neutron_sudoers /etc/sudoers.d/neutron_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_neutron_extend_start  
RUN chmod 755 /usr/local/bin/kolla_neutron_extend_start \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/neutron_sudoers \  
&& usermod -a -G kolla neutron  
  
USER neutron

