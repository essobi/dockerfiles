FROM debian:jessie  
ADD docker-entrypoint.sh /  
RUN mkdir -p /var/run/sshd && \  
chmod +x docker-entrypoint.sh && \  
apt-get update && \  
apt-get install -y proftpd supervisor openssh-server && \  
echo 'RootLogin on' >> /etc/proftpd/proftpd.conf  
COPY sshd_config /etc/ssh/sshd_config  
COPY proftpd.conf /etc/proftpd/proftpd.conf  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

