FROM debian:jessie  
  
# Set desired borg version  
ENV BORGVERSION=1.1.4  
# Set variables  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install dependencies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
build-essential \  
fuse \  
libacl1 \  
libacl1-dev \  
libfuse-dev \  
liblz4-1 \  
liblz4-dev \  
liblzma-dev \  
libssl-dev \  
openssh-server \  
openssl \  
pkg-config \  
python3 \  
python3-virtualenv \  
python3-dev \  
python3-pip  
  
RUN pip3 -v install 'llfuse<2.0'  
  
# Install borg  
RUN pip3 -v install borgbackup==${BORGVERSION}  
  
# Clean up  
RUN apt-get -y remove --purge build-essential libssl-dev liblz4-dev
libacl1-dev && \  
apt-get -y autoremove --purge && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup SSH Daemon  
ADD sshd_config /etc/ssh/sshd_config  
RUN rm -f /etc/ssh/ssh_host_*  
  
ADD start.sh /start.sh  
  
# Volume  
VOLUME /opt  
VOLUME /backups  
  
# Port  
EXPOSE 22  
# Command  
CMD ["/bin/bash", "/start.sh"]  

