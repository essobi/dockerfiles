FROM ubuntu:12.04  
  
MAINTAINER Sean Callan (@doomspork)  
  
RUN \  
groupadd docker ;\  
useradd -g docker docker  
  
# Basic dependencies  
RUN \  
echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list ;\  
apt-get update ;\  
apt-get upgrade -y ;\  
apt-get install -y wget \  
build-essential \  
python-software-properties \  
curl \  
git \  
vim \  
zsh  
  
# zsh + oh-my-zsh = <3  
RUN \  
wget –no-check-certificate https://github.com/robbyrussell/oh-my-
zsh/raw/master/tools/install.sh -O – | sh ;\  
chsh -s /bin/zsh  
  
  
# Ruby-install  
RUN \  
wget -O ruby-install-0.3.4.tar.gz --no-check-certificate
https://github.com/postmodern/ruby-install/archive/v0.3.4.tar.gz ;\  
tar -xzvf ruby-install-0.3.4.tar.gz ;\  
cd ruby-install-0.3.4 ;\  
make install ;\  
cd ;\  
rm -rf ruby-install-0.3.4/ ;\  
rm ruby-install-0.3.4.tar.gz  
  
RUN ruby-install -i /opt/rubies/ruby-2.0.0-p353 ruby 2.0.0-p353  
  
# Let's make our PATH  
ENV PATH
/opt/rubies/ruby-2.0.0-p353/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN gem install bundler

