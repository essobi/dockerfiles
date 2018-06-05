FROM debian:stable  
  
RUN \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y -q update \  
&& apt-get -y -q --no-install-recommends install \  
curl \  
ca-certificates \  
gosu \  
redis-server \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /var/log/dpkg.log \  
&& curl -#L
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 -o /usr/local/bin/confd \  
&& chmod 755 /usr/local/bin/confd \  
&& mkdir -p /etc/confd/conf.d \  
&& mkdir -p /etc/confd/templates \  
&& touch /etc/confd/confd.toml  
  
EXPOSE 6379  
ENV LANG=C  
  
COPY confd/redis.toml /etc/confd/conf.d/  
COPY confd/templates/redis.conf.tmpl /etc/confd/templates/  
#RUN /usr/local/bin/confd -onetime -backend env  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["redis"]  

