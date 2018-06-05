FROM rocker/r-base  
  
RUN wget --no-check-certificate -O -
https://github.com/basho/basho_bench/archive/master.tar.gz | tar -C /tmp -xz  
RUN mkdir /app && mv /tmp/basho_bench-master/priv /app/priv  
RUN Rscript --vanilla /app/priv/common.r  
  
WORKDIR /app  
CMD Rscript --vanilla priv/summary.r -i tests/current  

