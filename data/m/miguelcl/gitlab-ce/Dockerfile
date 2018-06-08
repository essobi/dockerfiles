FROM ubuntu:xenial  
MAINTAINER miguel corzo  
# Enviroment variable declaration  
ENV LOG_NETWORK_PATH="" \  
DATA_NETWORK_PATH="" \  
CONFIG_NETWORK_PATH="" \  
NETWORK_USER="" \  
NETWORK_USER_PASSWORD=""  
# Install required packages, add samba package  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
ca-certificates \  
openssh-server \  
wget \  
apt-transport-https \  
vim \  
nano \  
cifs-utils \  
curl  
COPY gitStart.sh /  
# Manage SSHD through runit & Disabling use DNS in ssh since it tends to slow
connecting  
RUN mkdir -p /opt/gitlab/sv/sshd/supervise \  
&& mkdir /GitInstallDir /etc/gitlab /var/log/gitlab /var/opt/gitlab \  
&& mkfifo /opt/gitlab/sv/sshd/supervise/ok \  
&& printf "#!/bin/sh\nexec 2>&1\numask 077\nexec /usr/sbin/sshd -D" >
/opt/gitlab/sv/sshd/run \  
&& chmod a+x /opt/gitlab/sv/sshd/run \  
&& ln -s /opt/gitlab/sv/sshd /opt/gitlab/service \  
&& mkdir -p /var/run/sshd \  
&& echo "UseDNS no" >> /etc/ssh/sshd_config \  
&& cd /GitInstallDir \  
&& wget https://packages.gitlab.com/gitlab/gitlab-
ce/packages/ubuntu/xenial/gitlab-ce_8.9.9-ce.0_amd64.deb/download --output-
document=gitlab-ce_8.9.9-ce.0_amd64.deb \  
&& chmod +x /gitStart.sh  
# Expose web & ssh  
EXPOSE 443 80 22  
# Run gitInstall.sh  
CMD /gitStart.sh

