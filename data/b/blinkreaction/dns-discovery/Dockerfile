FROM alpine:3.4  
MAINTAINER Leonid Makarov <leonid.makarov@blinkreaction.com>  
  
RUN apk add --no-cache \  
curl \  
supervisor \  
dnsmasq \  
&& rm -rf /var/cache/apk/*  
  
# Install docker-gen  
ENV DOCKER_GEN_VERSION 0.7.3  
ENV DOCKER_GEN_TARFILE docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz  
RUN curl -sSL https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/$DOCKER_GEN_TARFILE -O && \  
tar -C /usr/local/bin -xvzf $DOCKER_GEN_TARFILE && \  
rm $DOCKER_GEN_TARFILE  
  
# dnsmasq config dir  
RUN mkdir -p /etc/dnsmasq.d && \  
echo -e '\nconf-dir=/etc/dnsmasq.d,.tmpl' >> /etc/dnsmasq.conf  
  
COPY conf/dnsmasq.tmpl /etc/dnsmasq.d/dockergen.tmpl  
COPY conf/supervisord.conf /etc/supervisor.d/docker-gen.ini  
COPY entrypoint.sh /opt/entrypoint.sh  
  
# Default domain and IP for wildcard query resolution  
ENV DNS_DOMAIN 'drude'  
ENV DNS_IP '192.168.10.10'  
ENV LOG_QUERIES false  
  
EXPOSE 53/udp  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
  
CMD ["supervisord", "-n"]  

