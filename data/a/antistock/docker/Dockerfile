FROM pritunl/archlinux:2016-07-16  
MAINTAINER Roman Scherer <roman@burningswell.com>  
  
ENV LEIN_ROOT 1  
ENV PACMAN_OPTS --noconfirm --noprogressbar  
ENV PATH "$PATH:/usr/bin/site_perl:/usr/bin/vendor_perl"  
RUN pacman -S $PACMAN_OPTS cpanminus curl gcc make jdk8-openjdk rabbitmq
postgis postgresql sudo && pacman -Scc $PACMAN_OPTS  
  
RUN curl
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein  
RUN chmod 755 /usr/local/bin/lein  
RUN lein version  
  
RUN cpanm --notest App::Sqitch DBD::Pg  
  
RUN pacman -S $PACMAN_OPTS git fakeroot jshon expac && \  
pacman -Scc $PACMAN_OPTS && \  
curl https://aur.archlinux.org/cgit/aur.git/snapshot/packer.tar.gz | tar xz -C
/tmp && \  
cd /tmp/packer && \  
chown nobody.nobody /tmp/packer && \  
sudo -u nobody makepkg && \  
pacman -U --noconfirm /tmp/packer/packer-*-any.pkg.tar.xz && \  
rm -rf /tmp/packer && \  
echo "packer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
useradd -m -g users -s /bin/bash packer  
  
RUN sudo -u packer packer --noconfirm -S zookeeper  

