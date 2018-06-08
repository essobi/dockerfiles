FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
RUN yum -y install httpd mod_wsgi python-ldappool python-rados && yum clean
all  
RUN mkdir -p /var/www/cgi-bin/gnocchi \  
&& sed -i -r 's,^(Listen 80),#\1,' /etc/httpd/conf/httpd.conf  
  
RUN mkdir -p /gnocchi-base-source && git clone
git://git.openstack.org/openstack/gnocchi /gnocchi-base-source/gnocchi-base &&
pushd /gnocchi-base-source/gnocchi-base && git checkout
2b1ed8d4528df8c3071343d1cd5764b6a7122fd1 && popd  
  
  
RUN ln -s gnocchi-base-source/* gnocchi \  
&& useradd --user-group gnocchi \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt gnocchiclient
/gnocchi[keystone,mysql,file,ceph] \  
&& mkdir -p /etc/gnocchi /var/log/kolla/gnocchi /home/gnocchi \  
&& cp -r /gnocchi/etc/gnocchi/* /etc/gnocchi/ \  
&& chown -R gnocchi: /etc/gnocchi /var/log/kolla/gnocchi  
  
  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
COPY gnocchi_sudoers /etc/sudoers.d/kolla_gnocchi_sudoers  
  
RUN usermod -a -G kolla gnocchi \  
&& mkdir -p /var/lib/gnocchi \  
&& chown -R gnocchi: /var/lib/gnocchi \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_gnocchi_sudoers \  
&& touch /usr/local/bin/kolla_gnocchi_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_gnocchi_extend_start  

