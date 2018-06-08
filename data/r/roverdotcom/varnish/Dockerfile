FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
curl \  
vim \  
apt-transport-https \  
supervisor \  
&& curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - \  
&& echo "deb https://repo.varnish-cache.org/ubuntu/ precise varnish-4.1" \  
>> /etc/apt/sources.list.d/varnish-cache.list \  
&& apt-get update && apt-get install -y varnish \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV VCL_CONFIG=/etc/varnish/default.vcl \  
CACHE_SIZE=64m \  
VARNISHD_PARAMS="-p default_ttl=3600 -p default_grace=3600"  
COPY default.vcl /etc/varnish/default.vcl  
COPY supervisor.conf /supervisor.conf  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-c", "/supervisor.conf"]  

