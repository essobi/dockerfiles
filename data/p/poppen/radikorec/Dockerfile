FROM phusion/baseimage:0.9.18  
MAINTAINER MATSUI Shinsuke <poppen.jp@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common \  
&& add-apt-repository ppa:mc3man/trusty-media \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ffmpeg \  
swftools \  
build-essential \  
gcc \  
make \  
git \  
libssl-dev \  
unzip \  
libxml2-utils \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp/work  
RUN git clone git://git.ffmpeg.org/rtmpdump \  
&& curl -L
https://github.com/K-S-V/Scripts/releases/download/v2.4/rtmpdump-2.4.zip >
/tmp/work/rtmpdump-2.4.zip \  
&& unzip -x rtmpdump-2.4.zip \  
&& cd rtmpdump \  
&& patch -p0 < ../Patch.diff \  
&& make SYS=posix \  
&& make install \  
&& ldconfig \  
&& rm -rf /tmp/work  
  
WORKDIR /  
  
ADD
https://gist.githubusercontent.com/poppen/93fe4d09f3fca0113139bf1e8d9d48c3/raw/rec_radiru.sh
/usr/local/bin/  
ADD
https://gist.githubusercontent.com/poppen/1da36e6e5671df2c273d2c24e4ad23a7/raw/rec_radiko.sh
/usr/local/bin/  
RUN chmod 0755 /usr/local/bin/rec_radiru.sh \  
&& chmod 0755 /usr/local/bin/rec_radiko.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

