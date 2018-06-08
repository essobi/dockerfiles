FROM virtuman/nginx-php-exim:latest  
  
COPY . /app/  
  
RUN apt-get update && \  
apt-get install -yqq sudo && \  
apt-get clean && \  
rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
#&& \  
# chmod 750 /app/bin/* && \  
# /app/bin/install_phpmd.sh && \  
# /app/bin/install_phploc.sh && \  
# /app/bin/install_phpunit.sh && \  
# /app/bin/install_phpcs.sh  
ENTRYPOINT []  
  

