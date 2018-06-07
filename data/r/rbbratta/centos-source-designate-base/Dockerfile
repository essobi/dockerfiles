FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /designate-base-source && git clone
git://git.openstack.org/openstack/designate /designate-base-source/designate-
base && pushd /designate-base-source/designate-base && git checkout
c0c599b2f5ea861f515e82ec8b1dad30c11e2575 && popd  
  
RUN ln -s designate-base-source/* designate \  
&& useradd \--user-group designate \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install \--upgrade -c
requirements/upper-constraints.txt /designate \  
&& mkdir -p /etc/designate /var/log/designate /home/designate \  
&& cp -r /designate/etc/designate/* /etc/designate/ \  
&& mv /etc/designate/rootwrap.conf.sample /etc/designate/rootwrap.conf \  
&& chown -R designate: /etc/designate /var/log/designate /home/designate \  
&& sed -i
's|^exec_dirs.*|exec_dirs=/var/lib/kolla/venv/bin,/sbin,/usr/sbin,/bin,/usr/bin,/usr/local/bin,/usr/local/sbin|g'
/etc/designate/rootwrap.conf  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN touch /usr/local/bin/kolla_designate_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_designate_extend_start  
  
  
  
  
  
RUN usermod -a -G kolla designate

