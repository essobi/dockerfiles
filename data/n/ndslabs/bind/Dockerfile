FROM ubuntu:xenial  
  
RUN apt-get update -y && \  
apt-get install -y bind9* bind9-host dnsutils vim \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
EXPOSE 53/udp 53/tcp 10000/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["named"]  

