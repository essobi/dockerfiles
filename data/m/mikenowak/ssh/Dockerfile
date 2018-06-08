FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND "noninteractive"  
ENV PACKAGES "openssh-server vim groff less host irssi screen unzip bzip2
ipcalc pwgen git-core awscli jq wget curl ca-certificates locales"  
ENV LOCALE "en_US.utf8 en_GB.utf8 pl_PL.UTF-8 ja_JP.UTF-8"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends $PACKAGES \  
&& rm -f /etc/ssh/ssh_host_* \  
&& mkdir -p /var/run/sshd \  
&& groupadd ssh-users \  
&& locale-gen $LOCALE \  
&& rm -fr /var/lib/apt/lists/*  
  
COPY sshd_config /etc/ssh/sshd_config  
COPY sshd-pam.d /etc/pam.d/sshd  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME ["/etc/ssh/hostkeys", "/home"]  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 22  

