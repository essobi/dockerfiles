FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install lvm2 qemu-img ceph-common && yum clean all  
  
RUN mkdir -p /cinder-base-source && git clone
git://git.openstack.org/openstack/cinder /cinder-base-source/cinder-base &&
pushd /cinder-base-source/cinder-base && git checkout
ab9518112137f3141739e873b19cdc0085963bc7 && popd  
  
RUN ln -s cinder-base-source/* cinder \  
&& useradd \--user-group cinder \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /cinder \  
&& mkdir -p /etc/cinder /var/lib/cinder /home/cinder \  
&& cp -r /cinder/etc/cinder/* /etc/cinder/ \  
&& chown -R cinder: /etc/cinder /var/lib/cinder /home/cinder \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/cinder/rootwrap.conf  
  
  
  
COPY cinder_sudoers /etc/sudoers.d/kolla_cinder_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla cinder \  
&& mkdir -p /etc/ceph \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_cinder_sudoers \  
&& touch /usr/local/bin/kolla_cinder_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_cinder_extend_start  

