  
FROM embox/emdocker  
MAINTAINER Anton Kozlov <drakon.mega@gmail.com>  
  
RUN apt-get update  
  
# x86/test/fs nfs  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
nfs-kernel-server \  
nfs-common  
  
RUN mkdir -p -m 777 /var/nfs_test  
COPY exports /etc/  
  
# x86/test/fs cifs  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
samba  
  
RUN mkdir -p -m 777 /var/cifs_test  
COPY smb.conf /etc/samba/  
  
# x86/test/net  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
net-tools \  
isc-dhcp-server \  
iputils-ping \  
telnet \  
ntp \  
openbsd-inetd  
  
COPY dhcpd.conf /etc/dhcp/  
COPY isc-dhcp-server /etc/default/  
COPY ntp.conf /etc/  
  
RUN useradd -u 65534 -o -ms /bin/bash rlogin_user  
RUN /bin/echo -e "rlogin\nrlogin" | passwd rlogin_user  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
psmisc  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install \  
wget \  
expect \  
snmp  
  
CMD mount -t tmpfs none /var/nfs_test && \  
service rpcbind restart && \  
/etc/init.d/nfs-kernel-server restart && \  
/etc/init.d/nmbd restart && \  
/etc/init.d/smbd restart && \  
/etc/init.d/ntp restart && \  
inetd && \  
/usr/local/sbin/docker_start.sh  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt /var/cache/apt  
  

