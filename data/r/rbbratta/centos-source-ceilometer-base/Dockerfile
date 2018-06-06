FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /ceilometer-base-source && git clone
git://git.openstack.org/openstack/ceilometer /ceilometer-base-
source/ceilometer-base && pushd /ceilometer-base-source/ceilometer-base && git
checkout 8c1e5366d8ed1539acab681551469ec49e37dc68 && popd  
  
RUN ln -s ceilometer-base-source/* ceilometer \  
&& useradd \--user-group ceilometer \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /ceilometer[gnocchi,mongo,mysql] \  
&& mkdir -p /etc/ceilometer /var/lib/ceilometer /home/ceilometer \  
&& cp -r /ceilometer/etc/ceilometer/* /etc/ceilometer/ \  
&& chown -R ceilometer: /etc/ceilometer /var/lib/ceilometer /home/ceilometer \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/ceilometer/rootwrap.conf  
  
  
  
COPY ceilometer_sudoers /etc/sudoers.d/kolla_ceilometer_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla ceilometer \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_ceilometer_sudoers \  
&& touch /usr/local/bin/kolla_ceilometer_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_ceilometer_extend_start

