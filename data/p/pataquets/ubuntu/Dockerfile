FROM ubuntu:bionic  
  
# Use a local APT caching proxy, if available  
ADD ./etc/apt/ /etc/apt/  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install apt-transport-https && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
bash-completion \  
netcat-traditional \  
ssl-cert \  
&& \  
cat /etc/bash_completion | tee /etc/bash.bashrc && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y upgrade && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -v \  
/etc/ssl/certs/ssl-cert-snakeoil.pem \  
/etc/ssl/private/ssl-cert-snakeoil.key \  
&& \  
mkdir -vp /var/log/symlinks/dev/ && \  
mkdir -vp /var/log/symlinks/proc/self/fd && \  
ln -s /dev/stdout /var/log/symlinks/dev/stdout && \  
ln -s /dev/stderr /var/log/symlinks/dev/stderr && \  
ln -s /proc/self/fd/1 /var/log/symlinks/proc/self/fd/1 && \  
ln -s /proc/self/fd/2 /var/log/symlinks/proc/self/fd/2  

