FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install openvswitch && yum clean all  
  
RUN mkdir -p /manila-base-source && git clone
git://git.openstack.org/openstack/manila /manila-base-source/manila-base &&
pushd /manila-base-source/manila-base && git checkout
8f2fa31d8a47e52b01bcf48771da83c23da464b1 && popd  
  
RUN ln -s manila-base-source/* manila \  
&& useradd --user-group manila \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /manila \  
&& mkdir -p /etc/manila /var/lib/manila /var/cache/manila /home/manila \  
&& cp -r /manila/etc/manila/* /etc/manila/ \  
&& chown -R manila: /etc/manila /var/lib/manila /var/cache/manila /home/manila
\  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/manila/rootwrap.conf  
  
COPY manila_sudoers /etc/sudoers.d/kolla_manila_sudoers  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_manila_sudoers  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_manila_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_manila_extend_start  
  
RUN usermod -a -G kolla manila  
  

