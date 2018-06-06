FROM swiftnetworks/docker-php-cli-7  
RUN apt-get update && apt-get install -y \  
nodejs \  
npm \  
node-less \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
WORKDIR /var/www/html  
  
CMD ["-"]  
  
ENTRYPOINT ["/var/www/html/bin/console"]  

