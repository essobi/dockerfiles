FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND=noninteractive \  
GLUSTER_VOLUMES='' \  
GLUSTER_HOST=''  
  
RUN apt-get update \  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 3FE869A9 \  
&& echo "deb http://ppa.launchpad.net/gluster/nfs-ganesha/ubuntu xenial main"
> /etc/apt/sources.list.d/nfs-ganesha.list \  
&& echo "deb http://ppa.launchpad.net/gluster/libntirpc/ubuntu xenial main" >
/etc/apt/sources.list.d/libntirpc.list \  
&& apt-get update -q \  
&& apt-get install -y wget unzip uuid-runtime python-setuptools udev runit
sharutils nfs-common \  
dbus nfs-ganesha nfs-ganesha-fsal software-properties-common glusterfs-
client/xenial nfs-kernel-server -q \  
&& add-apt-repository ppa:gluster/glusterfs-3.8 \  
&& apt-get update -q \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /run/rpcbind /export /var/run/dbus \  
&& touch /run/rpcbind/rpcbind.xdr /run/rpcbind/portmap.xdr \  
&& chmod 777 /run/rpcbind/* \  
&& chown messagebus:messagebus /var/run/dbus \  
&& apt-get clean  
  
# Add startup script  
COPY entrypoint.sh /entrypoint.sh  
  
# NFS ports and portmapper  
EXPOSE 2049 38465-38467 662 111/udp 111  
  
# Start Ganesha NFS daemon and mount all Gluster Volumes  
CMD ["/entrypoint.sh"]  
  

