FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /trove-base-source && git clone
git://git.openstack.org/openstack/trove /trove-base-source/trove-base && pushd
/trove-base-source/trove-base && git checkout
345a7eb196ab0b9fcfd55c2c5b6f573d9b4e2caa && popd  
  
RUN ln -s trove-base-source/* trove \  
&& useradd \--user-group trove \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /trove \  
&& mkdir -p /etc/trove /var/log/trove /home/trove \  
&& cp -r /trove/etc/* /etc/trove/ \  
&& chown -R trove: /etc/trove /var/log/trove /home/trove  
  
  
  
RUN usermod -a -G kolla trove  
  

