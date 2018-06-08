FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /mistral-base-source && git clone
git://git.openstack.org/openstack/mistral /mistral-base-source/mistral-base &&
pushd /mistral-base-source/mistral-base && git checkout
6356bce81417102accb3619aa05129ab35a35dad && popd  
  
RUN ln -s mistral-base-source/* mistral \  
&& useradd --user-group mistral \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install /mistral \  
&& mkdir -p /etc/mistral /home/mistral \  
&& cp -r /mistral/etc/* /etc/mistral/ \  
&& chown -R mistral: /etc/mistral /home/mistral  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
  
RUN usermod -a -G kolla mistral \  
&& touch /usr/local/bin/kolla_mistral_extend_start \  
&& chmod 755 /usr/local/bin/kolla_extend_start
/usr/local/bin/kolla_mistral_extend_start

