FROM ubuntu:xenial  
MAINTAINER Ben Meekhof <bmeekhof@umich.edu>  
  
# install prerequisites  
RUN DEBIAN_FRONTEND=noninteractive \  
&& echo "deb http://download.ceph.com/nfs-ganesha/deb-V2.5-stable/luminous
xenial main" > /etc/apt/sources.list.d/nfs-ganesha-2.5.list \  
&& echo "deb http://download.ceph.com/debian-luminous xenial main" >
/etc/apt/sources.list.d/ceph-luminous.list \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated sssd libnss-sss netbase
krb5-user nfs-common libnfsidmap2 dbus libcephfs2 nfs-ganesha nfs-ganesha-ceph
nfs-ganesha-rgw libntirpc1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /run/rpcbind /export /var/run/dbus \  
&& touch /run/rpcbind/rpcbind.xdr /run/rpcbind/portmap.xdr \  
&& chmod 755 /run/rpcbind/* \  
&& chown messagebus:messagebus /var/run/dbus  
  
# Add startup script  
COPY start.sh /  
  
# NFS ports and portmapper  
EXPOSE 2049 38465-38467 662 111/udp 111  
# Start Ganesha NFS daemon by default  
CMD ["/start.sh"]  

