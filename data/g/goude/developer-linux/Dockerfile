FROM ubuntu:xenial  
MAINTAINER Daniel Goude <daniel@goude.se>  
EXPOSE 22  
  
RUN \  
apt-get update && \  
apt-get install -y \  
apt-transport-https \  
build-essential \  
cifs-utils \  
cmake \  
curl \  
exuberant-ctags \  
git \  
gnupg \  
hdevtools \  
htop \  
libaio1 alien \  
libbz2-dev \  
libcurl4-openssl-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
locales \  
openssh-server \  
samba-client \  
silversearcher-ag \  
software-properties-common \  
sudo \  
tmux \  
tree \  
zlib1g-dev \  
zsh \  
jq \  
golang \  
ghc \  
pandoc \  
postgresql-client \  
openjdk-8-jre-headless && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E298A3A825C0D65DFD57CBB651716619E084DAB9 && \  
add-apt-repository 'deb [arch=amd64,i386]
https://cran.rstudio.com/bin/linux/ubuntu xenial/' && \  
add-apt-repository ppa:neovim-ppa/stable && \  
apt-get update && \  
apt-get install -y neovim r-base && \  
mkdir -p /var/run/sshd && \  
locale-gen en_US.UTF-8 && \  
useradd -ms /usr/bin/zsh runcom && \  
echo "runcom:runcom" | chpasswd && \  
adduser runcom sudo && \  
apt-get clean && \  
echo "developer-linux $(date --iso-8601=seconds)" >> /home/runcom/.runcom-log
&& \  
chown runcom:runcom /home/runcom/.runcom-log  
  
#python-dev \  
#python3-dev python3-pip python3-venv \  
#python3-lxml \  
#python3-cairo \  
#python3-matplotlib python3-pandas \  
#python3-sklearn \  

