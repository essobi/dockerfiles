FROM redis  
  
MAINTAINER Zeyu Ye <Shuliyey@gmail.com>  
  
ARG GIDDYUP_VERSION=0.17.1  
RUN apt-get update \  
&& apt-get install -y curl openssl ca-certificates wget \  
&& update-ca-certificates \  
&& mkdir -p /usr/local/etc/redis \  
&& cd /usr/local/etc/redis \  
&& ((grep -E "^ *net.core.somaxconn *= *.*$" /etc/sysctl.conf && sed -i -E
"s/^ *net.core.somaxconn *= *.*$/net.core.somaxconn=511/g" /etc/sysctl.conf)
|| echo "net.core.somaxconn=511" >> /etc/sysctl.conf) \  
&& ((grep -E "^ *vm.overcommit_memory *= *.*$" /etc/sysctl.conf && sed -i -E
"s/^ *vm.overcommit_memory *= *.*$/vm.overcommit_memory=1/g" /etc/sysctl.conf)
|| echo "vm.overcommit_memory=1" >> /etc/sysctl.conf) \  
&& wget http://download.redis.io/redis-stable/sentinel.conf \  
&& chown redis:redis /usr/local/etc/redis/sentinel.conf \  
&& wget
https://github.com/rancher/giddyup/releases/download/v${GIDDYUP_VERSION}/giddyup
-P /usr/local/bin \  
&& chmod +x /usr/local/bin/giddyup  
  
RUN rm -rf ~/* \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD docker-entrypoint.sh /  
  
WORKDIR /data  
  
EXPOSE 6379 16379 26379  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["redis-server", "/usr/local/etc/redis/sentinel.conf", "--sentinel"]  

