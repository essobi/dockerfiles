FROM pataquets/collectd  
  
RUN \  
ln -vs /etc/collectd/conf-available/write-csv-stdout.conf \  
/etc/collectd/conf.d/ \  
&& \  
nl \  
/etc/collectd/collectd.conf \  
/etc/collectd/conf.d/*  

