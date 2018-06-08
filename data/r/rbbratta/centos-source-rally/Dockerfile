FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /rally-source && git clone
git://git.openstack.org/openstack/rally /rally-source/rally && pushd /rally-
source/rally && git checkout a40248f9b8e70b76a0c1f1076a59d8cdfc8dc86a && popd  
  
RUN ln -s rally-source/* rally \  
&& useradd --user-group rally \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /rally \  
&& mkdir -p /etc/rally /var/log/rally /home/rally \  
&& chown -R rally: /etc/rally /var/log/rally /home/rally  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla rally  
  
USER rally

