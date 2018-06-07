FROM ubuntu:14.04  
MAINTAINER Ludovic Courtois <ludovic@lcourtois.fr>  
  
RUN apt-get update && \  
apt-get install -y git-core && \  
apt-get install -y gcc-avr binutils-avr avr-libc make  
  
RUN git clone https://github.com/dolu89/ergodox-firmware.git firmware  
  
VOLUME /keymap  
  
COPY start.sh /  
  
CMD [ "./start.sh" ]  

