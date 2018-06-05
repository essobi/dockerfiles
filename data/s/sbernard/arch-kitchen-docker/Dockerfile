FROM base/archlinux:latest  
MAINTAINER Samuel Bernard "samuel.bernard@gmail.com"  
# Let's run stuff  
RUN \  
# First, update everything (start by keyring and pacman)  
pacman -Sy && \  
pacman -S archlinux-keyring --noconfirm && \  
pacman -S pacman --noconfirm && \  
pacman-db-upgrade && \  
pacman -Su --noconfirm && \  
# Install Git  
pacman -S git --noconfirm && \  
# Install Docker  
pacman -S docker --noconfirm && \  
# Install kmod for Docker  
pacman -S kmod --noconfirm && \  
# It quite common to need to interact with S3  
pacman -S s3cmd --noconfirm && \  
# Install what is needed for building native extensions  
pacman -S gcc make sed awk gzip grep autoconf automake --noconfirm && \  
# Install useful tools  
pacman -S vim tree iproute2 inetutils --noconfirm && \  
# Install Ruby and Gems  
pacman -S ruby --noconfirm && \  
gem install test-kitchen berkshelf kitchen-docker_cli bundler \  
\--no-user-install --no-rdoc --no-ri && \  
# Install Foodcritic and Rubocop  
gem install foodcritic rubocop --no-user-install --no-rdoc --no-ri && \  
# Generate locale en_US (workaround for a strange bug in berkshelf)  
locale-gen en_US.UTF-8 && \  
# Time to clean  
pacman -Scc --noconfirm  
  
ENV LANG=en_US.UTF-8  
CMD ["/usr/bin/bash"]  

