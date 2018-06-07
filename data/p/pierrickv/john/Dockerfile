FROM debian:stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update -qq && apt install -y \  
git \  
build-essential \  
libssl-dev \  
python \  
zlibc \  
libghc-zlib-dev \  
&& git clone --depth=1 https://github.com/magnumripper/JohnTheRipper.git \  
&& cd JohnTheRipper/src \  
&& ./configure \  
&& make clean \  
&& make -s \  
&& chmod +x /JohnTheRipper/run/john \  
&& ln -s /JohnTheRipper/run/john /usr/bin/john \  
&& apt remove -y \  
git \  
build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR "/JohnTheRipper/run/"  

