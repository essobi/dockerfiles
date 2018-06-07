FROM debian:jessie  
RUN apt-get update && \  
apt-get install nullidentd -y && \  
apt-get upgrade -y && \  
apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /usr/share/locale/* && \  
rm -rf /var/cache/debconf/*-old && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc/*  
  
COPY inetd.conf /etc/  
  
EXPOSE 113  
  
CMD ["/usr/sbin/inetd","-i"]  

