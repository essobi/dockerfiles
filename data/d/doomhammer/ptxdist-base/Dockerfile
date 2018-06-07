FROM debian  
MAINTAINER Piotr Gaczkowski <DoomHammerNG@gmail.com>  
  
RUN apt-get update && \  
apt-get install -qqy \  
automake \  
bison \  
bzip2 \  
fakeroot \  
file \  
flex \  
gawk \  
gcc \  
g++ \  
gettext \  
git \  
libconfuse-dev \  
libncurses-dev \  
make \  
patch \  
pkg-config \  
python-dev \  
texinfo \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /usr/src && \  
cd /usr/src && \  
wget http://www.pengutronix.de/software/genimage/download/genimage-7.tar.xz &&
\  
tar xf genimage-7.tar.xz && \  
cd genimage-7 && \  
./configure && \  
make && \  
make install && \  
cd /usr/src && \  
git clone git://git.pengutronix.de/git/ptxdist.git  

