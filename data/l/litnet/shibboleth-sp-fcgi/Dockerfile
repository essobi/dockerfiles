FROM debian:latest  
  
RUN apt-get -y update && \  
apt-get -y --no-install-recommends install \  
ca-certificates \  
openssl \  
shibboleth-sp2-utils \  
supervisor 1>/dev/null && \  
rm -r /var/lib/apt/lists/* && \  
/usr/sbin/shib-keygen -f 1>/dev/null && \  
mkdir -p /var/log/shibboleth && \  
mv /etc/shibboleth /etc/shibboleth-orig  
  
COPY etc/supervisor/conf.d/shibd-supervisor.conf /etc/supervisor/conf.d/shibd-
supervisor.conf  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
WORKDIR /etc/shibboleth  
  
VOLUME ["/etc/shibboleth"]  
  
EXPOSE 8118/TCP 9119/TCP  
  
CMD ["docker-entrypoint.sh"]  
  

