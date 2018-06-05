FROM ubuntu  
MAINTAINER Christopher Bunn  
  
RUN apt-get update  
  
# Install just enough to get rolling  
RUN apt-get install -y \  
curl \  
vim \  
zsh \  
git \  
build-essential \  
man-db \  
htop \  
iftop \  
iotop \  
tar \  
unzip \  
zip \  
zlib1g-dev  
  
# Install python dependencies  
RUN apt-get install -y \  
autotools-dev \  
blt-dev \  
bzip2 \  
dpkg-dev \  
g++-multilib \  
gcc-multilib \  
libbluetooth-dev \  
libbz2-dev \  
libexpat1-dev \  
libffi-dev \  
libffi6 \  
libffi6-dbg \  
libgdbm-dev \  
libgpm2 \  
libncursesw5-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtinfo-dev \  
mime-support \  
net-tools \  
netbase \  
python-crypto \  
python-mox3 \  
python-pil \  
python-ply \  
quilt \  
tk-dev \  
zlib1g-dev  
  
# Install latest python 2  
RUN (cd ~/ && \  
curl https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz | tar -xz && \  
cd Python-2.7.11 && \  
./configure && \  
make && \  
make install && \  
cd ~/ && \  
rm -rf Python-2.7.11)  
  
# Install my dotfiles  
RUN bash -c "$(curl -fsSL
https://raw.githubusercontent.com/mypetyak/dotfiles/master/install.sh)"  
  
# Install PIP  
RUN curl https://bootstrap.pypa.io/get-pip.py | python  
  
# Install global PIP packages  
RUN pip install cheat  
  
# Cleanup unnecessary files  
RUN apt-get clean  

