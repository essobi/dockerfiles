FROM percona:5.6  
  
RUN apt-get update \  
&& apt-get install -y libjemalloc1 \  
&& apt-get install -y percona-server-tokudb-5.6  
  
ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libjemalloc.so.1  

