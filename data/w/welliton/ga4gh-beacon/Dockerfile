FROM debian:jessie  
  
WORKDIR /usr/lib/cgi-bin/  
  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends git python \  
ca-certificates apache2 libpng12-0 && \  
a2enmod cgi && \  
git clone https://github.com/maximilianh/ucscBeacon.git && \  
mv ucscBeacon beacon && \  
apt-get remove --yes git ca-certificates && \  
rm -rf /var/lib/apt/lists/* && \  
mv beacon/utils/bottleneck /usr/local/bin/ && \  
rmdir beacon/utils/ && \  
bottleneck start  
  
COPY index.html /var/www/html/  
COPY docker-ga4gh-beacon-entrypoint /usr/local/bin/  
  
EXPOSE 80  
ENTRYPOINT ["docker-ga4gh-beacon-entrypoint"]  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

