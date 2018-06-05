FROM ubuntu:16.04  
  
MAINTAINER Marcos Oliveira Soares <marcosoliveirasoares94@gmail.com>  
  
#  
# Labels  
#  
LABEL name = "marcosoliveirasoares94/ubuntu:16.04" \  
summary = "Ubuntu 16 Image with OpenSSH-Server." \  
description = "Ubuntu 16 Image with OpenSSH-Server." \  
ssh-root-user="root" \  
ssh-root-password="secret" \  
ssh-developer-user="developer" \  
ssh-developer-password="developer" \  
applications="vim tar zip ftp sed curl less nano wget unzip net-tools openssh-
server openssh-client supervisor libcurl4-openssl-dev software-properties-
common"  
#  
# Environment variables.  
#  
ENV TERM=xterm  
ENV SSH_ROOT_USER=root  
ENV SSH_ROOT_PASSWORD=secret  
ENV SSH_DEVELOPER_USER=developer  
ENV SSH_DEVELOPER_PASSWORD=developer  
ENV UBUNTU_FRONTEND=noninteractive  
  
#  
# BASE image installation.  
#  
RUN apt-get update -y && apt-get install -y \  
vim \  
tar \  
zip \  
ftp \  
sed \  
curl \  
less \  
nano \  
wget \  
sudo \  
whois \  
unzip \  
net-tools \  
apt-utils \  
supervisor \  
iputils-ping \  
openssh-server \  
openssh-client \  
libcurl4-openssl-dev \  
software-properties-common && \  
#  
# Removing outdated software.  
#  
apt-get autoclean && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/*  
  
#  
# SSH Configurations developer  
#  
RUN useradd -d /home/${SSH_DEVELOPER_USER} -G sudo -k /etc/skel -m -s
/bin/bash ${SSH_DEVELOPER_USER} && \  
echo "${SSH_DEVELOPER_USER}:${SSH_DEVELOPER_PASSWORD}" | chpasswd && \  
#  
# SSH Configurations root  
#  
echo "${SSH_ROOT_USER}:${SSH_ROOT_PASSWORD}" | chpasswd && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -i 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' /etc/pam.d/sshd && \  
#  
# SSH Configuration Directory  
#  
mkdir -p /var/run/sshd && \  
#  
# Terminal Configuration  
#  
echo 'alias ls="ls -a --color=auto"' >> /etc/bash.bashrc && \  
echo 'alias ll="ls -la --color=auto"' >> /etc/bash.bashrc && \  
sudo sed -i 's/env_reset/env_reset,pwfeedback/g' /etc/sudoers && \  
#  
# Timezone  
#  
echo 'America/Sao_Paulo' > /etc/timezone  
  
#  
# Copy File  
#  
COPY conf/supervisord.conf /etc/supervisord.conf  
  
#  
# Solving the error of: Too Many Files Open  
#  
COPY conf/sysctl.conf /etc/sysctl.conf  
COPY conf/limits.conf /etc/security/limits.conf  
COPY conf/90-nproc.conf /etc/security/limits.d/90-nproc.conf  
  
#  
# Expose Port  
#  
EXPOSE 20 21 22  
#  
# Default command  
#  
CMD ["/usr/bin/supervisord"]  

