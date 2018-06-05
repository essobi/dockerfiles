# Sources used: https://github.com/silvio/docker-borgbackup,
https://github.com/tgbyte/docker-borg-backup  
# Create a directory in /var/backups called "borg" in order to put the
repository (server side)  
# Will be the base to the server and the client version of the container  
FROM debian:jessie  
  
MAINTAINER Sebastien Collin <sebastien.collin@sebcworks.fr>  
  
# Prepare environment, create user, etc...  
ENV BORGVERSION=1.0.11  
ENV LANG C.UTF-8  
RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime  
  
RUN adduser --disabled-password --gecos "Borg Backup" \--quiet borg && \  
mkdir -p /var/run/sshd && \  
mkdir -p /var/backups/borg && \  
mkdir -p /home/borg/.ssh && \  
mkdir -p /home/borg/data  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -y \  
&& apt-get install -y \  
build-essential \  
fuse \  
libacl1-dev \  
libfuse-dev \  
liblz4-dev \  
liblzma-dev \  
libssl-dev \  
openssh-server \  
pkg-config \  
python3-virtualenv \  
python3-dev \  
python3-pip \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Some more clean  
RUN rm -f /etc/ssh/ssh_host_*  
  
# Python dependencies (for client)  
RUN pip3 -v --log=/var/log/pip-install.log install 'llfuse<0.41'  
  
# Clone Borg repository  
RUN pip3 -v --log=/var/log/pip-install.log install "borgbackup>=$BORGVERSION"
&& \  
apt-get remove -y --purge build-essential libssl-dev libacl1-dev && \  
apt-get autoremove -y --purge  
  
# Entrypoint and command are not important here  
COPY docker-borg-entrypoint.sh /borg-entrypoint.sh  
  
ENTRYPOINT ["/borg-entrypoint.sh"]  
CMD ["echo","Borg Backup"]  

