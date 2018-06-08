FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN yum -y install python-rbd python-rados && yum clean all  
  
RUN mkdir -p /glance-base-source && git clone
git://git.openstack.org/openstack/glance /glance-base-source/glance-base &&
pushd /glance-base-source/glance-base && git checkout
4404ae6a7e2b8d96db102ada8aaf07cbc92e256b && popd  
  
RUN ln -s glance-base-source/* glance \  
&& useradd --user-group glance \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /glance[cinder] \  
&& mkdir -p /etc/glance /var/lib/glance /home/glance \  
&& cp -r /glance/etc/* /etc/glance/ \  
&& chown -R glance: /etc/glance /var/lib/glance /home/glance  
  
COPY glance_sudoers /etc/sudoers.d/kolla_glance_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla glance \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 440 /etc/sudoers.d/kolla_glance_sudoers \  
&& touch /usr/local/bin/kolla_glance_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_glance_extend_start  
  

