FROM debian:stretch  
  
RUN apt-get update && apt-get install -y linux-perf && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mv /usr/bin/perf_4.4 /usr/bin/perf  
ENTRYPOINT ["/usr/bin/perf"]  

