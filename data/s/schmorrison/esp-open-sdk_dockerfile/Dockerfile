FROM debian:7.8  
#RUN echo 'Acquire::http { Proxy "http://172.17.0.2:3142"; };' >>
/etc/apt/apt.conf.d/01proxy  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# unrar is non-free  
RUN "echo" "deb http://http.us.debian.org/debian wheezy non-free" >>
/etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
autoconf \  
automake \  
bison \  
build-essential \  
bzip2 \  
flex \  
g++ \  
gawk \  
gcc \  
git \  
gperf \  
help2man \  
libexpat-dev \  
libtool \  
make \  
ncurses-dev \  
nano \  
python \  
python-dev \  
python-serial \  
sed \  
texinfo \  
unrar \  
unzip \  
wget  
  
RUN useradd -m espbuilder \  
&& usermod -a -G dialout espbuilder \  
&& usermod -a -G uucp espbuilder  
  
USER espbuilder  
  
ADD heatshrink_config.h /home/espbuilder/heatshrink_config.h  
ADD Makefile /home/espbuilder/Makefile  
  
##sed -e 's/2.1.0/2.2.0/g' crosstool-NG/config/companion_libs/expat.in && \  
  
RUN cd /home/espbuilder \  
&& git clone --recursive https://github.com/pfalcon/esp-open-sdk.git \  
&& cd /home/espbuilder/esp-open-sdk \  
&& make STANDALONE=y \  
&& cp /home/espbuilder/esp-open-sdk/xtensa-lx106-elf/bin/xtensa-lx106-elf-nm
/home/espbuilder/esp-open-sdk/xtensa-lx106-elf/bin/xt-nm \  
&& ls  
  
ENV PATH /home/espbuilder/esp-open-sdk/xtensa-lx106-elf/bin:$PATH  
  
RUN cd /home/espbuilder/ \  
&& git clone --recursive https://github.com/schmorrison/cleanflo-esphttpd \  
&& cd /home/espbuilder/cleanflo-esphttpd/mkespfsimage \  
&& make  
  
RUN cd /home/espbuilder/ \  
&& mv /home/espbuilder/cleanflo-esphttpd/lib/heatshrink/heatshrink_config.h \  
/home/espbuilder/cleanflo-esphttpd/lib/heatshrink/heatshrink_config.h.bak \  
&& cp /home/espbuilder/heatshrink_config.h /home/espbuilder/cleanflo-
esphttpd/lib/heatshrink/heatshrink_config.h \  
&& cd cleanflo-esphttpd \  
&& make clean \  
&& make  
  
WORKDIR /home/espbuilder/newfirmware  

