# Ubuntu ready to be Jenkins Slave  
#  
# Oracle Java  
# Ansible  
# Docker client  
# Docker Compose  
# Docker Machine  
# Shade (Clients for OpenStack)  
# OpenSSH  
  
FROM winggundamth/ubuntu-java:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install Git, Ansible, OpenSSH and necessary packages  
# 2) Download Docker client, machine and compose  
# 3) Clean to reduce size of Docker Image  
ARG APT_CACHER_NG  
ARG DEVPI_SERVER  
ENV ANSIBLE_HOST_KEY_CHECKING=False  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
[ -n "$DEVPI_SERVER" ] && \  
mkdir -p ~/.pip && \  
echo "[global]\n\  
index-url = $DEVPI_SERVER\n\  
trusted-host = \  
$(echo $DEVPI_SERVER | awk -F/ '{print $3}' | awk -F: '{print $1}')\n\  
" >> ~/.pip/pip.conf || true; \  
apt-get update && \  
apt-get install -y git python python-dev curl wget git build-essential \  
openssh-server vim tmux rsync byobu libssl-dev libffi-dev && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install ansible boto docker-py dnspython shade && \  
wget -O /usr/local/bin/docker.tgz \  
https://get.docker.com/builds/Linux/x86_64/docker-1.12.0.tgz && \  
wget -O /usr/local/bin/docker-compose \  
https://github.com/docker/compose/releases/download/1.8.0/docker-
compose-`uname -s`-`uname -m` && \  
wget -O /usr/local/bin/docker-machine \  
https://github.com/docker/machine/releases/download/v0.8.0/docker-
machine-`uname -s`-`uname -m` && \  
tar xvfz /usr/local/bin/docker.tgz -C /usr/local/bin/ \--strip=1 && \  
chmod +x /usr/local/bin/docker-compose /usr/local/bin/docker-machine && \  
apt-get remove --purge --auto-remove -y \  
build-essential ifupdown iproute2 isc-dhcp-client isc-dhcp-common \  
libatm1 libisc-export160 libmnl0 libxtables11 manpages netbase \  
libssl-dev libffi-dev && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy /root/.cache \  
/root/.pip /usr/local/bin/docker.tgz  
  
CMD ["/usr/sbin/sshd", "-D"]  
EXPOSE 22  
# 1) Configure OpenSSH  
# 2) Create jenkins user  
# 3) Prepare authorized_keys file for ssh  
# 4) Work around Ansible doesn't play very well with overlayfs  
# https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1214500  
ENV JENKINS_HOME=/var/jenkins  
RUN sed -i 's/required pam_loginuid.so/optional pam_loginuid.so/g' \  
/etc/pam.d/sshd && \  
echo 'export LC_ALL=en_US.UTF-8' > /root/.bash_profile && \  
useradd -s /bin/bash -d $JENKINS_HOME -m jenkins && \  
mkdir -p /var/run/sshd /root/.ssh $JENKINS_HOME/.ssh && \  
touch $JENKINS_HOME/.ssh/authorized_keys /root/.ssh/authorized_keys && \  
chown -R root:root /root/.ssh && \  
chown -R jenkins:jenkins $JENKINS_HOME/.ssh && \  
chmod 700 $JENKINS_HOME/.ssh /root/.ssh && \  
chmod 600 $JENKINS_HOME/.ssh/authorized_keys /root/.ssh/authorized_keys && \  
echo '[ssh_connection]' >> $JENKINS_HOME/.ansible.cfg && \  
echo 'ssh_args =' >> $JENKINS_HOME/.ansible.cfg  

