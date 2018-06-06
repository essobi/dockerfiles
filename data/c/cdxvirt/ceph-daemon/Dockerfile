# CEPH DAEMON IMAGE  
# CEPH VERSION: Jewel  
# CEPH VERSION DETAIL: 10.2.x  
FROM cdxvirt/ceph-base:base-10.2.10-2  
MAINTAINER Sébastien Han "seb@redhat.com"  
# Add bootstrap script, ceph defaults key/values for KV store  
ADD *.sh ceph.defaults check_zombie_mons.py ./osd_scenarios/* entrypoint.sh.in
/  
  
# Add bootstrap script, ceph defaults key/values for KV store  
ADD *.sh ceph.defaults check_zombie_mons.py ./osd_scenarios/* entrypoint.sh.in
disabled_scenario /  
  
# Modify the entrypoint  
RUN bash "/generate_entrypoint.sh" && \  
rm -f /generate_entrypoint.sh && \  
bash -n /*.sh  
  
# Add templates for confd  
ADD ./confd/templates/* /etc/confd/templates/  
ADD ./confd/conf.d/* /etc/confd/conf.d/  
  
# Add cdxvirt scripts  
ADD cdx /cdx  
RUN mv /cdx/ceph-api /usr/local/bin/ceph-api  
  
# Add volumes for Ceph config and data  
VOLUME ["/etc/ceph","/var/lib/ceph", "/etc/ganesha"]  
  
# Execute the entrypoint  
WORKDIR /  
ENTRYPOINT ["/entrypoint.sh"]  

