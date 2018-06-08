FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /murano-base-source && git clone
git://git.openstack.org/openstack/murano /murano-base-source/murano-base &&
pushd /murano-base-source/murano-base && git checkout
76e7d9e3ad5d7586fac6d686609f83701eb81036 && popd  
  
RUN ln -s murano-base-source/* murano \  
&& useradd --user-group murano \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /murano \  
&& mkdir -p /etc/murano /home/murano \  
&& cp -r /murano/etc/murano/* /etc/murano/ \  
&& chown -R murano: /etc/murano /home/murano \  
&& cd murano/meta/io.murano \  
&& zip -r /io.murano.zip *  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla murano \  
&& touch /usr/local/bin/kolla_murano_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_murano_extend_start  
  

