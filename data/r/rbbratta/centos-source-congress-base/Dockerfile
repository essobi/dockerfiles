FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /congress-base-source && git clone
git://git.openstack.org/openstack/congress /congress-base-source/congress-base
&& pushd /congress-base-source/congress-base && git checkout
fcccfb24dd9f999899be02430fd70305920a7104 && popd  
  
RUN ln -s congress-base-source/* congress \  
&& useradd --user-group congress \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /congress \  
&& mkdir -p /etc/congress /home/congress \  
&& cp -r /congress/etc/* /etc/congress/ \  
&& chown -R congress: /etc/congress /home/congress  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla congress \  
&& touch /usr/local/bin/kolla_congress_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_congress_extend_start  
  

