FROM perfectweb/base:v2  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
RUN git clone -b linux https://github.com/tpruvot/cpuminer-multi.git  
RUN cd /cpuminer-multi && ./build.sh  
  
ENTRYPOINT ["/cpuminer-multi/cpuminer"]  
CMD ["-a", "lbry", "-o", "stratum+tcp://lbry.suprnova.cc:6256", "-u",
"Tahity.default", "-p", "x"]  

