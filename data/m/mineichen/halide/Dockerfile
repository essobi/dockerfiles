FROM mineichen/llvm:3.8.1  
  
ENV HALIDE_VERSION 2016_10_25  
  
RUN apt-get update \  
&& apt-get install -y make g++ libpng-dev libz-dev \  
&& addgroup halide \  
&& adduser --ingroup halide --system halide \  
&& mkdir -p /root/build/halide_src \  
&& mkdir -p /root/build/halide_dist \  
&& echo $LD_LIBRARY_PATH \  
&& cd /root/build/ \  
&& wget -O halide.tar.gz
https://github.com/halide/Halide/archive/release_${HALIDE_VERSION}.tar.gz \  
&& tar -zxf halide.tar.gz -C halide_src --strip-components=1 \  
&& cd halide_dist \  
&& make distrib -f ../halide_src/Makefile \  
&& mv distrib/lib/libHalide.a /usr/lib/x86_64-linux-gnu/ \  
&& mv bin/libHalide.so /usr/lib/x86_64-linux-gnu/ \  
&& mkdir /usr/include/halide && mv distrib/include/* /usr/include/halide \  
&& mv distrib/tools/*.h /usr/include/halide/ \  
&& rm -rf /root/build \  
&& apt-get clean  
  
WORKDIR /home/halide  
  

