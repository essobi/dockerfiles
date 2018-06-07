FROM php:5.6  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get clean && \  
rm -rf /var/lib/lists/*  
  
RUN wget http://deployer.org/deployer.phar && \  
mv deployer.phar /usr/local/bin/dep && \  
chmod +x /usr/local/bin/dep  
  
WORKDIR /app  
ENTRYPOINT ["/usr/local/bin/dep"]  

