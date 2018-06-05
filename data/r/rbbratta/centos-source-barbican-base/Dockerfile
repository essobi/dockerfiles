FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
  
  
RUN yum -y install uwsgi-plugin-python && yum clean all  
  
RUN mkdir -p /barbican-base-source && git clone
git://git.openstack.org/openstack/barbican /barbican-base-source/barbican-base
&& pushd /barbican-base-source/barbican-base && git checkout
d29569882f74542595451bebab66b22be7b5dcde && popd  
  
RUN ln -s barbican-base-source/* barbican \  
&& useradd --user-group barbican \  
&& /var/lib/kolla/venv/bin/pip \--no-cache-dir install --upgrade -c
requirements/upper-constraints.txt pastedeploy uwsgi MySQL-python python-
barbicanclient /barbican \  
&& mkdir -p /etc/barbican /var/log/barbican /home/barbican /var/lib/barbican \  
&& cp -r /barbican/etc/barbican/* /etc/barbican/ \  
&& chown -R barbican: /etc/barbican /var/log/barbican /home/barbican
/var/lib/barbican  
  
  
  
COPY barbican_sudoers /etc/sudoers.d/kolla_barbican_sudoers  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla barbican \  
&& chmod 750 /etc/sudoers.d \  
&& chmod 640 /etc/sudoers.d/kolla_barbican_sudoers \  
&& touch /usr/local/bin/kolla_barbican_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_barbican_extend_start  

