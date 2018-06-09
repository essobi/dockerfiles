FROM dock0/full_arch:latest  
  
MAINTAINER Leonardo Nodari <nodarileonardo@gmail.com>  
  
# Make docker more real  
RUN pacman -Syu && \  
pacman -S --noconfirm systemd && \  
pacman -Sc --noconfirm && \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
RUN pacman -S --noconfirm sudo networkmanager  
  
# Disable requiretty.  
RUN sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
# Append needed parameters to sudo env  
RUN sed -i '/# Defaults mail_badpass/a Defaults env_keep = "HOME"'
/etc/sudoers  
  
# Create user, home directory & add it to sudoers  
RUN useradd -m valet \  
&& echo "valet ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/valet  
  
# Install Dependences  
RUN pacman -Syu --noconfirm \  
nginx curl zip unzip git php-fpm  
  
# Fix "pid" directive is duplicate in /etc/nginx/nginx.conf  
RUN sed -i "s/PIDFile=.*//" /usr/lib/systemd/system/nginx.service && \  
sed -i "s/ExecStart=.*/ExecStart=\/usr\/bin\/nginx -g 'error_log stderr;'/"
/usr/lib/systemd/system/nginx.service  
# Configure environment  
RUN echo "PATH=\"\$HOME/.composer/vendor/bin:\$PATH\"" >> /home/valet/.profile
\  
&& echo 'export USER=$(whoami)' >> /home/valet/.profile  
  
# Insert prepare script  
ADD prepare.sh /  
RUN chmod +x /prepare.sh  
  
CMD ["/sbin/init"]  

