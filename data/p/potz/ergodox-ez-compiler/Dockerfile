FROM debian:jessie  
  
MAINTAINER Potiguar Faga <potz@potz.me>  
  
# Installs requirements for compiling the firmware  
RUN apt-get update && \  
apt-get install -y git-core && \  
apt-get install -y gcc-avr binutils-avr avr-libc make && \  
apt-get install -y dfu-programmer dfu-util && \  
rm -rf /var/lib/apt/lists/*  
  
# Specify which SHA and branch from jack humbert's  
# firmware repository we want to fetch  
ENV SHA a258358b6c2df0d1347a6506831076ef6a9784b3  
ENV BRANCH master  
  
RUN git clone -q --branch=$BRANCH https://github.com/jackhumbert/qmk_firmware
/firmware && \  
cd /firmware && git checkout -f $SHA && \  
cd /firmware/keyboards/ergodox/ez && make clean  
  
# Map this volume to some folder where a keymap.c can be found.  
# The resulting firmware.hex will also be put in this folder when finished.  
VOLUME /keymap  
  
COPY entrypoint.sh /  
  
CMD [ "./entrypoint.sh" ]  

