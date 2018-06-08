FROM ubuntu:trusty  
MAINTAINER Andreas Böhrnsen <andreas@frontrunner.io>  
  
ENV DEV_USERNAME frontrunner  
  
# Disable root password  
RUN passwd -l root  
  
# Create user and give sudo  
RUN \  
/bin/bash -c '\  
useradd --create-home -s /bin/bash $DEV_USERNAME && \  
adduser $DEV_USERNAME sudo && \  
mkdir -p /etc/sudoers.d && \  
echo $DEV_USERNAME ALL=NOPASSWD:ALL > /etc/sudoers.d/$DEV_USERNAME && \  
chmod 0440 /etc/sudoers.d/$DEV_USERNAME \  
'  
  
# Install essential tools  
RUN \  
apt-get update && \  
apt-get install -yy --no-install-recommends \  
build-essential \  
ca-certificates \  
cmake \  
curl \  
git \  
libpq-dev \  
libssl-dev \  
libreadline-dev \  
zlib1g-dev && \  
apt-get clean  
  
# Install nvm and rbenv in user space  
USER $DEV_USERNAME  
  
# install nvm  
RUN \  
/bin/bash -c '\  
git clone https://github.com/creationix/nvm.git ~/.nvm && \  
cd ~/.nvm && git checkout v0.29.0 && \  
echo "# nvm" >> ~/.bashrc && \  
echo "export NVM_DIR=\"\$HOME/.nvm\"" >> ~/.bashrc && \  
echo "[ -s \"\$NVM_DIR/nvm.sh\" ] && . \"\$NVM_DIR/nvm.sh\"" >> ~/.bashrc \  
'  
  
# Install rbenv  
RUN \  
/bin/bash -c '\  
git clone https://github.com/sstephenson/rbenv.git ~/.rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-
build && \  
echo "# rbenv" >> ~/.bashrc && \  
echo "export PATH=\"\$HOME/.rbenv/bin:\$PATH\"" >> ~/.bashrc && \  
echo "eval \"\$(rbenv init -)\"" >> ~/.bashrc \  
'  
  
USER root  
  
# Install dev tools  
RUN \  
apt-get update && \  
apt-get install -yy --no-install-recommends \  
curl \  
git \  
silversearcher-ag \  
tig \  
tmux \  
vim-nox \  
wget \  
zsh && \  
apt-get clean  
  

