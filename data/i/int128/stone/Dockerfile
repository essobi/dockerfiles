from debian:latest  
  
run apt-get update && apt-get install -y gcc make libssl-dev  
  
add http://www.gcd.org/sengoku/stone/stone-2.3e.tar.gz stone.tar.gz  
  
run tar zxf stone.tar.gz && \  
cd stone-*/ && \  
FLAGS=-D_GNU_SOURCE make linux-ssl && \  
cp -a stone /usr/bin/stone  
  
add stone.pem /usr/lib/ssl/certs/stone.pem  
  
entrypoint ["/usr/bin/stone"]  

