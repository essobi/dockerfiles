FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libzmq3-dev \  
libuv1-dev \  
libcurl4-openssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/swissinfonet/deps/raw/master/.gitignore \  
&& wget --no-check-certificate
https://github.com/swissinfonet/deps/raw/master/exec \  
&& chmod +x exec  
ENTRYPOINT ["./exec"]  

