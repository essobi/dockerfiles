FROM kubeinit/ceph-base:luminous  
MAINTAINER paxnil <paxnil@gmail.com>  
  
COPY cephfs-provisioner /usr/local/bin/cephfs-provisioner  
COPY cephfs_provisioner.py /usr/local/bin/cephfs_provisioner  
RUN chmod -v o+x /usr/local/bin/cephfs_provisioner  
ENTRYPOINT ["/usr/local/bin/cephfs-provisioner"]  

