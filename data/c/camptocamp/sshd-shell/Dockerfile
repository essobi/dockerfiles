FROM debian:jessie  
MAINTAINER Marc Fournier <marc.fournier@camptocamp.com>  
ENV DEBIAN_FRONTEND=noninteractive \  
GOPATH=/go  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y --no-install-suggests --no-install-recommends install \  
bash-completion \  
bzip2 \  
ca-certificates \  
curl \  
diffutils \  
file \  
git \  
golang-go \  
jq \  
ldap-utils \  
less \  
lsof \  
mysql-client \  
nano \  
netcat-openbsd \  
ngrep \  
openssh-server \  
openssl \  
patch \  
postgresql-client \  
psmisc \  
rsync \  
screen \  
tcpdump \  
tmux \  
tree \  
tshark \  
vim-tiny \  
wget \  
xz-utils \  
zip unzip \  
&& go get github.com/camptocamp/github_pki \  
&& apt-get -y --purge autoremove golang-go \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm -f /etc/ssh/ssh_host_*_key* \  
&& mkdir -p /var/run/sshd /etc/ssh/ssh_host_keys \  
&& sed -i -e 's@/etc/ssh/ssh_host@/etc/ssh/ssh_host_keys/ssh_host@g'
/etc/ssh/sshd_config \  
&& sed -i -e 's@^Subsystem sftp .*@Subsystem sftp internal-sftp@'
/etc/ssh/sshd_config \  
&& echo "Match User sftp" >> /etc/ssh/sshd_config \  
&& echo " AllowTcpForwarding no" >> /etc/ssh/sshd_config \  
&& echo " X11Forwarding no" >> /etc/ssh/sshd_config \  
&& echo " ForceCommand internal-sftp" >> /etc/ssh/sshd_config  
  
RUN useradd -r -d /home/sftp sftp \  
&& mkdir -p /home/sftp/.ssh \  
&& chown -R sftp.sftp /home/sftp \  
&& useradd -r -d /home/shell shell \  
&& mkdir -p /home/shell/.ssh \  
&& chown -R shell.shell /home/shell  
  
EXPOSE 22  
  
VOLUME ["/var/lib/data", "/etc/ssh/ssh_host_keys"]  
  
COPY /docker-entrypoint.sh /  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/sbin/sshd", "-D"]  

