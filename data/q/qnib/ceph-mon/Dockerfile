FROM qnib/ceph-base  
  
ADD etc/supervisord.d/ceph-mds.ini /etc/supervisord.d/  
ADD etc/consul.d/ceph-mon.json /etc/consul.d/  
ADD opt/qnib/ceph/mon/bin/*.sh /opt/qnib/ceph/mon/bin/  

