FROM fedora:25  
  
MAINTAINER Leonardo Nodari <nodarileonardo@gmail.com>  
  
# Make docker more real  
RUN dnf -y update && dnf -y install systemd && dnf clean all && \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
RUN dnf -y install sudo which NetworkManager  
  
# Disable requiretty.  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# Append needed parameters to sudo env  
RUN sed -i '/Defaults secure_path/a Defaults env_keep = "HOME"' /etc/sudoers  
  
# Create user, home directory & add it to sudoers  
RUN useradd -m valet \  
&& echo "valet ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/valet  
  
# Install Dependences  
RUN dnf makecache fast \  
&& dnf -y install \  
nginx jq curl zip unzip git \  
php-fpm php-cli php-mcrypt php-mbstring php-xml php-curl php-posix \  
&& dnf clean all  
  
# Configure environment  
RUN echo "PATH=\"\$HOME/.composer/vendor/bin:\$PATH\"" >> /home/valet/.profile
\  
&& echo 'export USER=$(whoami)' >> /home/valet/.profile  
  
# Insert prepare script  
ADD prepare.sh /  
RUN chmod +x /prepare.sh  
  
VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]  
CMD ["/usr/sbin/init"]  

