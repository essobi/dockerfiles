FROM rbbratta/centos-source-ironic-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
RUN mkdir -p /ironic-inspector-source && git clone
git://git.openstack.org/openstack/ironic-inspector /ironic-inspector-
source/ironic-inspector && pushd /ironic-inspector-source/ironic-inspector &&
git checkout f33658a2b4aee7e9049aca4bc4fba26e6d60848a && popd  
  
RUN ln -s ironic-inspector-source/* ironic-inspector \  
&& mv /etc/ironic /etc/ironic-inspector \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /ironic-inspector \  
&& cp /ironic-inspector/rootwrap.conf /etc/ironic-inspector/ \  
&& cp -r /ironic-inspector/rootwrap.d/ /etc/ironic-inspector/ \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/ironic-inspector/rootwrap.conf  
  
  
  
COPY ironic_sudoers /etc/sudoers.d/kolla_ironic_inspector_sudoers  
RUN chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_ironic_inspector_sudoers  
  
  
  
  
  
USER ironic

