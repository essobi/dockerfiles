FROM hectcastro/basho-otp  
  
RUN curl -L https://github.com/basho/basho_bench/archive/master.tar.gz | tar
-C /tmp -xz  
RUN cd /tmp/basho_bench-master && make all  
RUN mv /tmp/basho_bench-master/basho_bench /usr/local/bin/basho_bench  
  
WORKDIR /app  

