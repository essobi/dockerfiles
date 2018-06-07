FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /ironic-base-source && git clone
git://git.openstack.org/openstack/ironic /ironic-base-source/ironic-base &&
pushd /ironic-base-source/ironic-base && git checkout
3f54fec070fdc0e7a63083eb0630b1d37005c30c && popd  
  
RUN ln -s ironic-base-source/* ironic \  
&& useradd \--user-group \--create-home \--home-dir /var/lib/ironic ironic \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /ironic \  
&& mkdir -p /etc/ironic /var/lib/ironic \  
&& cp -r /ironic/etc/ironic/* /etc/ironic/ \  
&& chown -R ironic: /etc/ironic /var/lib/ironic \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/ironic/rootwrap.conf  
  
ADD ironic_sudoers /etc/sudoers.d/kolla_ironic_sudoers  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_ironic_sudoers  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN touch /usr/local/bin/kolla_ironic_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_ironic_extend_start \  
&& usermod -a -G kolla ironic \  
&& chown -R ironic: /etc/ironic  

