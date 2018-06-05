FROM golang  
  
RUN apt-get update && apt-get install -y \  
cmake \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://boringssl.googlesource.com/boringssl /boringssl \  
&& mkdir /boringssl/build \  
&& cd /boringssl/build \  
&& cmake .. \  
&& make \  
&& mv /boringssl/build/tool/bssl /usr/local/bin/ \  
&& rm -rf /boringssl \  
&& apt-get remove -y --purge --auto-remove \  
cmake \  
&& strip /usr/local/bin/bssl  

