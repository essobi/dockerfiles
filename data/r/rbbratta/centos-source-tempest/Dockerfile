FROM rbbratta/centos-source-openstack-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /tempest-source && git clone git://github.com/redhat-
openstack/tempest.git /tempest-source/tempest && pushd /tempest-source/tempest
&& git checkout aaff550edab124a744b2888bcf7a7d70d3abfa0c && popd  
  
# NOTE(Jeffrey4l): remove the tempest version constraint in the  
# upper-constrains.txt file. Otherwise, it will be failed.  
RUN ln -s tempest-source/* tempest \  
&& sed -i 's/^tempest===.*$//' requirements/upper-constraints.txt \  
&& /var/lib/kolla/venv/bin/pip --no-cache-dir install --upgrade -c
requirements/upper-constraints.txt /tempest \  
&& mkdir -p /etc/tempest /var/log/tempest /etc/tempest/tempest_lock  
  
WORKDIR /tempest  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start  
  

