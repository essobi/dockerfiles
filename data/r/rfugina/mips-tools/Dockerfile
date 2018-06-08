  
FROM ubuntu:wily  
  
MAINTAINER Rob Fugina <robf@fugina.com>  
  
RUN apt-get update && apt-get -y dist-upgrade \  
&& apt-get install -y --force-yes --no-install-recommends software-properties-
common \  
&& apt-add-repository ppa:angelsl/mips-cross \  
&& apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends \  
gcc-5-mips-linux-gnu \  
libc6-dev-mips-cross \  
gcc-5-mipsel-linux-gnu \  
libc6-dev-mipsel-cross \  
build-essential \  
qemu-user \  
&& for f in `ls /usr/bin/mips*-linux-gnu-*-5`; do ln -vs $f `echo $f | sed -e
's/-5$//'`; done \  
&& apt-get install -y --force-yes --no-install-recommends \  
file \  
git \  
less \  
man \  
perl \  
vim \  
libcommon-sense-perl \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
ENTRYPOINT /bin/bash  
  

