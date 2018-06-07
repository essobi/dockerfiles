FROM debian:jessie  
MAINTAINER Samuel Bernard "samuel.bernard@gmail.com"  
# Let's run stuff  
RUN \  
# Classic yum update  
apt-get update; apt-get dist-upgrade -y; \  
  
# Mask failing services  
systemctl mask -- \  
sys-fs-fuse-connections.mount \  
dev-hugepages.mount \  
systemd-tmpfiles-setup.service; \  
  
# Useful packages  
apt-get install -y iproute sudo less vim tree curl; \  
  
# Basic latest chef install  
curl -L https://omnitruck.chef.io/install.sh | bash; \  
ln -s /opt/chef/bin/chef-client /bin/chef-client; \  
  
# Installing Busser  
GEM_HOME="/tmp/verifier/gems" \  
GEM_PATH="/tmp/verifier/gems" \  
GEM_CACHE="/tmp/verifier/gems/cache" \  
/opt/chef/embedded/bin/gem install busser \--no-rdoc \--no-ri \  
\--no-format-executable -n /tmp/verifier/bin \--no-user-install; \  
  
# Busser plugins  
GEM_HOME="/tmp/verifier/gems" \  
GEM_PATH="/tmp/verifier/gems" \  
GEM_CACHE="/tmp/verifier/gems/cache" \  
/opt/chef/embedded/bin/gem install \  
busser-serverspec serverspec \--no-rdoc \--no-ri; \  
  
# Webmock can be very useful to test cookbooks  
GEM_HOME="/tmp/verifier/gems" \  
GEM_PATH="/tmp/verifier/gems" \  
GEM_CACHE="/tmp/verifier/gems/cache" \  
/opt/chef/embedded/bin/gem install \  
webmock \--no-rdoc \--no-ri; \  
  
# Last command, clean all  
apt-get clean autoclean  
  
VOLUME ["/sys/fs/cgroup", "/run", "/run/lock"]  
CMD ["/lib/systemd/systemd"]  

