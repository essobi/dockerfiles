FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
software-properties-common \  
apt-transport-https \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb [arch=amd64] https://mirrors.ripple.com/ubuntu/ trusty stable
contrib" \  
| sudo tee /etc/apt/sources.list.d/ripple.list  
RUN wget -O- -q https://mirrors.ripple.com/mirrors.ripple.com.gpg.key | sudo
apt-key add -  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
  
RUN apt-get update && apt-get -y upgrade && apt-get install -y \  
curl \  
git \  
scons \  
ctags \  
pkg-config \  
protobuf-compiler \  
libprotobuf-dev \  
libssl-dev \  
python-software-properties \  
boost-all-dev \  
nodejs \  
g++-5 \  
g++-4.9 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 99 --slave
/usr/bin/g++ g++ /usr/bin/g++-5  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 99 --slave
/usr/bin/g++ g++ /usr/bin/g++-4.9  
  
RUN mkdir /var/local/rippled  
RUN git clone -b 0.30.0 --single-branch https://github.com/ripple/rippled.git
/var/local/rippled  
  
WORKDIR "/var/local/rippled"  
RUN scons  
  
RUN apt-get update && apt-get install -y \  
npm \  
nodejs-legacy  
RUN npm install && npm test  

