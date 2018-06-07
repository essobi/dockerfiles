FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /heat-base-source && git clone
git://git.openstack.org/openstack/heat /heat-base-source/heat-base && pushd
/heat-base-source/heat-base && git checkout
dd707bc997715365dc76a3decea7b4f8d658375f && popd  
  
RUN ln -s heat-base-source/* heat \  
&& useradd --user-group heat \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /heat \  
&& mkdir -p /etc/heat /home/heat \  
&& cp -r /heat/etc/heat/* /etc/heat/ \  
&& chown -R heat: /etc/heat /home/heat  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla heat \  
&& touch /usr/local/bin/kolla_heat_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_heat_extend_start  
  

