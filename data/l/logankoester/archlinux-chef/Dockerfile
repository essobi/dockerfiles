# archlinux-chef  
# VERSION 1.3.0  
#  
# Arch Linux with Chef installed system-wide from Rubygems  
FROM logankoester/archlinux  
MAINTAINER Logan Koester <logan@logankoester.com>  
ENV CHEF_VERSION 12.8.1  
# Prepare the system  
USER root  
RUN pacman -S --noprogressbar --noconfirm --needed wget base-devel  
  
RUN mkdir -p /tmp/build  
RUN chown nobody:nobody -R /tmp/build && \  
chmod 775 -R /tmp/build && \  
echo "nobody ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Install ruby-bundler from AUR  
USER nobody  
WORKDIR /tmp/build  
RUN wget https://aur.archlinux.org/cgit/aur.git/snapshot/ruby-bundler.tar.gz
&& \  
tar -xzvf ruby-bundler.tar.gz  
WORKDIR /tmp/build/ruby-bundler  
RUN makepkg -i -s -f --noconfirm --noprogressbar  
  
USER root  
WORKDIR /  
RUN gem install chef --version $CHEF_VERSION \--no-user-install  
  
# Clean up  
RUN rm -f /var/lib/pacman/db.lck && \  
rm -rf /tmp/build && \  
sed -i '/nobody ALL=(ALL) NOPASSWD: ALL/d' /etc/sudoers  

