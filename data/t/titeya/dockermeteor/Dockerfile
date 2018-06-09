FROM debian:jessie  
  
RUN apt-get update  
  
# Install git, curl & npm compile tools  
RUN apt-get install -y curl make g++ gcc graphicsmagick && \  
(curl https://deb.nodesource.com/setup_8.x | sh) && \  
apt-get install -y nodejs jq && \  
apt-get clean && \  
rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/webapp && \  
chown -R www-data:www-data /var/webapp  
  
# Install entrypoint  
ADD entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
  
EXPOSE 80  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
CMD []  

