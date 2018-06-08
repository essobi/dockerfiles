# -*- dockerfile -*-  
# vim:ts=2 sw=2 et:  
  
FROM ubuntu  
MAINTAINER Vladimir Ermakov <vooon341@gmail.com>  
  
ENV OTA_VERSION 0.3.0  
ENV OTA_URL https://github.com/vooon/ota-mkfw/archive/${OTA_VERSION}.tar.gz  
  
ENV GCCARM_VERSION 5_2-2015q4  
ENV GCCARM_URL https://launchpad.net/gcc-arm-
embedded/5.0/5-2015-q4-major/+download/gcc-arm-none-
eabi-5_2-2015q4-20151219-linux.tar.bz2  
  
ENV PATH "$PATH:/opt/gcc-arm-none-eabi-${GCCARM_VERSION}/bin"  
# base deps  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
build-essential \  
git \  
make \  
python-empy \  
python-dateutil \  
python-setuptools \  
python-pip \  
python-dev \  
libffi-dev \  
libssl-dev \  
libc6-i386 \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# ota-mkfw  
RUN pip install "$OTA_URL"  
# arm-none-eabi toolchain  
RUN curl -SL "$GCCARM_URL" -o toolchain.tar.bz2 \  
&& tar -C /opt -xf toolchain.tar.bz2 \  
&& rm -f toolchain.tar.bz2  

