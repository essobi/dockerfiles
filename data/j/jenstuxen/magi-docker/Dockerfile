FROM resin/aarch64-debian  
#build arm packages using qemu on dockerhub  
RUN [ "cross-build-start" ]  
RUN apt-get update -y \  
&& apt-get install -y build-essential libcurl4-openssl-dev git autotools-dev
automake libgmp-dev \  
&& git clone https://github.com/magi-project/m-cpuminer-v2.git \  
&& cd m-cpuminer-v2/ \  
&& sed -i 's/-march=native/-march=armv8-a /' Makefile.am \  
&& ./autogen.sh \  
&& ./configure CFLAGS="-O3" CXXFLAGS="-O3" \  
&& make \  
&& make install \  
&& apt-get purge -y build-essential git automake autotools-dev \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& rm -rf /m-cpuminer-v2  
RUN [ "cross-build-end" ]  
  

