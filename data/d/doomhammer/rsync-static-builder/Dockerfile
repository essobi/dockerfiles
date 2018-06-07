# Use it to create a static rsync binary that is the sole occupant of a
container.  
# Useful for bootstrapping images hosted via rsync.  
#  
# To create an image containing static rsync binary run:  
# docker run doomhammer/rsync-static-builder | docker import -
doomhammer/rsync-static  
FROM debian  
MAINTAINER Piotr Gaczkowski <DoomHammerNG@gmail.com>  
  
RUN apt-get update && \  
apt-get install -qqy \  
automake \  
gcc \  
git \  
libpopt-dev \  
make \  
zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
cd /usr/src && \  
git clone git://git.samba.org/rsync.git && \  
cd rsync && \  
./configure --with-included-zlib=no --with-included-popt=no && \  
make CFLAGS="-static" EXEEXT="-static" && \  
strip rsync-static && \  
mkdir -p /newroot/usr/local/bin && \  
mv rsync-static /newroot/usr/local/bin/ && \  
rm -rf /usr/src/rsync  
  
CMD tar c -C /newroot .  

