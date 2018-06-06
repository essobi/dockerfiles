FROM rbbratta/centos-source-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
  
RUN yum -y install ceph ceph-radosgw parted hdparm btrfs-progs xfsprogs
e2fsprogs && yum clean all  
  
COPY extend_start.sh /usr/local/bin/kolla_extend_start  
RUN chmod 755 /usr/local/bin/kolla_extend_start \  
&& usermod -a -G kolla ceph  
  

