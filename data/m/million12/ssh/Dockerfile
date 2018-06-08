FROM million12/centos-supervisor  
  
ENV ROOT_PASS=password  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install --nogpgcheck -y \  
openssh-server \  
openssh-clients \  
pwgen \  
sudo \  
hostname \  
wget \  
patch \  
htop \  
iftop \  
vim \  
mc \  
links && \  
yum clean all && \  
  
ssh-keygen -q -b 1024 -N '' -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -b 1024 -N '' -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -b 521 -N '' -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key && \  
  
sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \  
sed -i -r
's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/'
/etc/ssh/sshd_config && \  
sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin yes/' /etc/ssh/sshd_config  
  
COPY container-files /  
  
EXPOSE 22  

