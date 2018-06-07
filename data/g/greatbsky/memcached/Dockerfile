FROM greatbsky/centos7  
MAINTAINER architect.bian  
LABEL name="memcached" license="MIT" build-date="20170221"  
  
ENV MEMCACHED_VERSION 1.4.34  
RUN yum update -y && yum install -y libevent-devel && groupadd -r memcache &&
useradd -r -g memcache memcache && cd /data/softs && wget -O memcached.tar.gz
https://memcached.org/latest && tar -zxf memcached.tar.gz && cd
memcached-$MEMCACHED_VERSION && ./configure --prefix=/usr/local/memcached &&
make && make install && rm -rf /data/softs/* && ln -s
/usr/local/memcached/bin/memcached /usr/bin/memcached  
  
USER memcache  
EXPOSE 11211  
CMD ["memcached", "-u memcache", "-p 11211", "-m 1024"]

