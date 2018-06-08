FROM esimone/mesos-centos-mesosphere  
  
RUN yum install -y mesos \  
&& yum \--enablerepo=* clean all \  
&& rm -rf /var/cache/yum  
  
RUN find /etc{,/default}/mesos{,-master,-slave} -type f -delete  

