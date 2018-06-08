FROM ubuntu:16.04  
MAINTAINER pastakhov@yandex.ru  
  
# Install requered packages  
# Install requered packages  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
varnish \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/archives/*  
  
ENV PROXY_PORT 80  
EXPOSE $PROXY_PORT  
  
COPY run-varnish.sh /run-varnish.sh  
RUN chmod -v +x /run-varnish.sh  
  
CMD ["/run-varnish.sh"]  

