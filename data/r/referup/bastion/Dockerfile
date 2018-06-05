FROM pataquets/sshd  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
screen \  
tmux \  
&& \  
apt-get clean && \  
locale-gen es_ES.UTF-8 && \  
dpkg-reconfigure locales && \  
rm -rf /var/lib/apt/lists/*  
  
#sshd_config security changes  
RUN \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin no/'
/etc/ssh/sshd_config && \  
echo 'Banner /etc/ssh/banner' >> /etc/ssh/sshd_config && \  
echo 'MaxAuthTries 3' >> /etc/ssh/sshd_config  

