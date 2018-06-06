# MkDocs  
# Cogset Open Source Group  
FROM debian:jessie  
  
MAINTAINER Cogset <cogset@funcuter.org>  
  
ENV MKDOCS_VERSION 0.16.1  
RUN buildDeps="wget" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends python python-pip $buildDeps \  
&& wget -O mkdocs.tar.gz
https://github.com/mkdocs/mkdocs/archive/$MKDOCS_VERSION.tar.gz \  
&& mkdir -p /usr/local/mkdocs \  
&& tar -xzf mkdocs.tar.gz -C /usr/local/mkdocs --strip-components=1 \  
&& rm -f certbot.tar.gz \  
&& pip install -e /usr/local/mkdocs \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /docs \  
&& mkdocs new /docs/src  
  
WORKDIR /docs/src  
  
VOLUME /docs/output  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8000  
CMD ["-s"]  

