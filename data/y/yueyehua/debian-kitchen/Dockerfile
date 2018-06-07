FROM yueyehua/debian-ruby  
MAINTAINER Richard Delaplace "rdelaplace@yueyehua.net"  
LABEL version="1.1.0"  
  
# Add Apt repositories  
RUN \  
curl -fsSL https://apt.dockerproject.org/gpg | apt-key add - && \  
add-apt-repository \  
"deb https://apt.dockerproject.org/repo/ debian-jessie main" && \  
apt-get -qq update;  
  
# Install docker  
RUN \  
apt-get -qq install -y docker-engine;  
  
# Clean all  
RUN \  
apt-get -qq clean autoclean;  
  
# Install test-kitchen  
RUN \  
gem install -q --no-rdoc --no-ri --no-format-executable --no-user-install \  
test-kitchen \  
kitchen-puppet \  
kitchen-ansible \  
kitchen-docker \  
kitchen-docker_cli;  
  
# Mask failing services  
RUN \  
systemctl mask -- \  
sys-fs-fuse-connections.mount \  
dev-hugepages.mount \  
systemd-tmpfiles-setup.service;  
  
VOLUME ["/sys/fs/cgroup", "/var/run/docker.sock", "/run", "/run/lock"]  
CMD ["/lib/systemd/systemd"]  

