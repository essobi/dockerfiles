FROM ubuntu:14.04  
  
RUN sed -i'~' -E
"s@http://(..\\.)?(archive|security)\\.ubuntu\\.com/ubuntu@http://ftp.jaist.ac.jp/pub/Linux/ubuntu@g"
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y less vim curl ca-certificates --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  

