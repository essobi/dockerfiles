FROM pataquets/collectd  
  
RUN \  
ls -Al /etc/collectd/conf-available/ && \  
cat \  
/etc/collectd/conf-available/global-FQDNLookup-disable.conf \  
/etc/collectd/conf-available/read-cpu.conf \  
/etc/collectd/conf-available/read-df-all.conf \  
/etc/collectd/conf-available/read-disk-all.conf \  
/etc/collectd/conf-available/read-load.conf \  
/etc/collectd/conf-available/read-memory.conf \  
/etc/collectd/conf-available/read-swap.conf \  
/etc/collectd/conf-available/read-uptime.conf \  
/etc/collectd/conf-available/read-vmem.conf \  
/etc/collectd/conf-available/write-network.conf \  
| tee -a /etc/collectd/collectd.conf \  
&& \  
nl /etc/collectd/collectd.conf  

