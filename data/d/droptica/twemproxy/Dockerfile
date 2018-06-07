FROM debian:8  
  
ENV VESRION 0.4.1  
  
RUN apt-get update && apt-get install --no-install-recommends -y \  
wget \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
  
&& wget --no-check-certificate
"https://drive.google.com/uc?export=download&id=0B6pVMMV5F5dfb1YwcThnaVZXbjg"
-O nutcracker-${VESRION}.tar.gz \  
  
&& tar zxf nutcracker-${VESRION}.tar.gz && rm nutcracker-${VESRION}.tar.gz \  
  
&& cd nutcracker-${VESRION} && ./configure && make && make install \  
  
&& cd .. && rm -rf nutcracker-${VESRION} \  
  
&& apt-get remove -y wget \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["nutcracker"]  
  
CMD []

