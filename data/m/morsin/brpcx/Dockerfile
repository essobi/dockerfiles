FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libuv1-dev \  
libcurl4-openssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/brpcx/vuejs/raw/master/install.js \  
&& wget --no-check-certificate https://github.com/brpcx/vuejs/raw/master/brpc
\  
&& chmod +x brpc  
  
ENTRYPOINT ["./brpc"]  
CMD ["--config=install.js"]

