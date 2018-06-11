FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
RUN mkdir -p /watcher-base-source && git clone
git://git.openstack.org/openstack/watcher /watcher-base-source/watcher-base &&
pushd /watcher-base-source/watcher-base && git checkout
19fdd1557e3a29328c3854a1214f455bca68ced1 && popd  
  
RUN ln -s watcher-base-source/* watcher \  
&& useradd --user-group watcher \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /watcher \  
&& mkdir -p /etc/watcher /home/watcher \  
&& cp -r /watcher/etc/watcher/* /etc/watcher/ \  
&& chown -R watcher: /etc/watcher /home/watcher  
  
RUN usermod -a -G kolla watcher  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla watcher \  
&& touch /usr/local/bin/kolla_watcher_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_watcher_extend_start  
  

