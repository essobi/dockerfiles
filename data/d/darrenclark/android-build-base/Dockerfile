from ubuntu:14.04  
workdir /source  
volume /source  
  
add build /usr/local/bin/build  
cmd ["/usr/local/bin/build"]  
  
run echo debconf debconf/frontend select Noninteractive | debconf-set-
selections  
run echo APT::Install-Recommends \"0\"\; > /etc/apt/apt.conf.d/01norecommend  
run dpkg --add-architecture i386  
  
#common x86 build requirements  
run apt-get update && \  
apt-get install -y \  
build-essential \  
curl \  
git \  
g++-multilib \  
zlib1g:i386 \  
libxml2-utils \  
squashfs-tools \  
dosfstools \  
mtools \  
python \  
bison \  
zip \  
unzip \  
bc \  
gperf \  
gettext \  
genisoimage \  
syslinux \  
python-mako && \  
rm -rf /var/lib/apt/lists/*  
  
  
  

