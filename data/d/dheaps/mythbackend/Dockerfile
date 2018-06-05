FROM dheaps/mythbackend:mythbuntu  
  
EXPOSE 80  
# Add files  
COPY files /root/  
# Install mythtvweb  
RUN apt-get install -y --no-install-recommends mythweb && \  
a2enmod headers && \  
a2enmod auth_digest && \  
# clean up  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  
CMD ["/root/dockerentry.sh"]

