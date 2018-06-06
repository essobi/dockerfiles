# Xunsearch  
# Cogset Open Source Group  
FROM debian:jessie  
  
MAINTAINER Cogset <cogset@funcuter.org>  
  
ENV XUNSEARCH_VERSION 1.4.10  
# Install  
RUN buildDeps="wget make gcc g++ bzip2 zlib1g-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& wget -O xunsearch.tar.bz2 "http://www.xunsearch.com/download/xunsearch-
full/xunsearch-full-$XUNSEARCH_VERSION.tar.bz2" \  
&& mkdir -p /usr/src/xunsearch \  
&& tar -xjf xunsearch.tar.bz2 -C /usr/src/xunsearch --strip-components=1 \  
&& rm xunsearch.tar.bz2 \  
&& cd /usr/src/xunsearch \  
&& sh setup.sh --prefix=/usr/local/xunsearch \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
  
VOLUME /usr/local/xunsearch/data  
  
WORKDIR /usr/local/xunsearch  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8383 8384  

