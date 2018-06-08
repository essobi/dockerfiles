FROM debian:jessie  
MAINTAINER Robin <robin@naas.io>  
  
ENV ACNG_VERSION 0.8.0-3  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r apt-cacher-ng && useradd -r -g apt-cacher-ng apt-cacher-ng  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
apt-cacher-ng="$ACNG_VERSION" \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /var/cache/apt-cacher-ng  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3142  
CMD ["/usr/sbin/apt-cacher-ng", "ForeGround=1"]

