FROM pataquets/ubuntu:trusty  
  
RUN \  
gpg --refresh-keys && \  
gpg --recv-key 3FE869A9 && \  
gpg --export \--armor | apt-key add - && \  
rm -vrf $HOME/.gnupg && \  
echo 'deb http://ppa.launchpad.net/gluster/glusterfs-3.6/ubuntu trusty main' >
/etc/apt/sources.list.d/glusterfs.list  

