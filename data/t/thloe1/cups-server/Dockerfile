FROM debian:stretch-slim  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends hplip && \  
rm -r /var/lib/apt/lists/* && \  
cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.docker  
  
VOLUME /etc/cups  
VOLUME /var/cache/cups  
VOLUME /var/spool/cups  
  
EXPOSE 631  
COPY entrypoint.sh /usr/local/sbin/  
  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD ["cupsd", "-f"]  

