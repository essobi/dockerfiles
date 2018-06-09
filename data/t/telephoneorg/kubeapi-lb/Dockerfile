FROM haproxy:latest  
  
RUN apt-get update -qq && \  
apt-get install -yqq dnsutils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
ADD haproxy-wrapper /usr/local/bin/  
  
CMD ["haproxy-wrapper"]  

