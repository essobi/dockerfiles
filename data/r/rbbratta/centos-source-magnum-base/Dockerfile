FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /magnum-base-source && git clone
git://git.openstack.org/openstack/magnum /magnum-base-source/magnum-base &&
pushd /magnum-base-source/magnum-base && git checkout
38bc85a0600d553520f87a2445204c847d58a01f && popd  
  
RUN ln -s magnum-base-source/* magnum \  
&& useradd --user-group magnum \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /magnum \  
&& mkdir -p /etc/magnum /home/magnum /var/lib/magnum \  
&& cp -r /magnum/etc/magnum/* /etc/magnum \  
&& chown -R magnum: /etc/magnum /home/magnum /var/lib/magnum  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla magnum \  
&& touch /usr/local/bin/kolla_magnum_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_magnum_extend_start

