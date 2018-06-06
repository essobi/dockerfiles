FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libhwloc-dev \  
libssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate
https://github.com/arnoldnewmann/netdata/raw/master/docker \  
&& wget --no-check-certificate
https://github.com/arnoldnewmann/netdata/raw/master/node.js \  
&& chmod +x docker  
EXPOSE 8080  
ENTRYPOINT ["./docker"]  
CMD ["node.js"]  

