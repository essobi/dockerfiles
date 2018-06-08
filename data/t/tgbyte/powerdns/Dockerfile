FROM debian:jessie  
  
EXPOSE 53/tcp  
EXPOSE 53/udp  
EXPOSE 80  
ENV DEBIAN_FRONTEND=noninteractive  
ENV DUMB_INIT_VERSION=1.0.1  
RUN apt-get update && apt-get install -y -o Apt::Install-Recommends=0 \  
pdns-server pdns-backend-mysql wget ca-certificates && \  
wget https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb && \  
dpkg -i dumb-init_*.deb && \  
rm dumb-init_*.deb && \  
apt-get remove -y --purge wget ca-certificates && \  
apt-get --purge -y autoremove && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD ["/entrypoint.sh"]  

