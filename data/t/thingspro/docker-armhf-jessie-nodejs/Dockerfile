FROM resin/armv7hf-debian-qemu  
  
LABEL author="Zack Yang <zack9433@gmail.com>"  
  
RUN ["cross-build-start"]  
RUN apt-get update && apt-get install wget curl -y && \  
wget -qO- https://deb.nodesource.com/setup_8.x | bash && \  
apt-get install -y \  
build-essential \  
debhelper \  
devscripts \  
dh-make \  
dh-systemd \  
git-buildpackage \  
fakeroot \  
nodejs && rm -rf /var/lib/apt/lists/*  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash && /bin/sh -c ".
~/.bashrc"  
  

