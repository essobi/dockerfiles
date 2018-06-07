FROM alpine:latest  
  
MAINTAINER unoexperto <unoexperto.support@mailnull.com>  
  
# python is necessary for ssdb-cli  
RUN apk update && \  
apk add gcc python && \  
apk add --virtual .build-deps autoconf make g++ git  
  
RUN mkdir -p /usr/src/ssdb  
  
RUN git clone \--depth 1 https://github.com/ideawu/ssdb.git /usr/src/ssdb && \  
make -C /usr/src/ssdb && \  
make -C /usr/src/ssdb install && \  
rm -rf /usr/src/ssdb  
  
RUN apk del .build-deps  
  
RUN mkdir /ssdb_data && \  
mkdir /ssdb_logs  
  
RUN sed \  
-e 's@work_dir = .*@work_dir = /ssdb_data@' \  
-e 's@pidfile = .*@pidfile = /var/run/ssdb.pid@' \  
-e 's@ip:.*@ip: 0.0.0.0@' \  
-e 's@cache_size:.*@cache_size: 4096@' \  
-e 's@write_buffer_size:.*@write_buffer_size: 512@' \  
-e 's@level:.*@level: info@' \  
-e 's@output:.*@output: /ssdb_logs/log.txt@' \  
-i /usr/local/ssdb/ssdb.conf  
  
EXPOSE 8888  
VOLUME /ssdb_data  
WORKDIR /ssdb_data  
  
CMD ["/usr/local/ssdb/ssdb-server", "/usr/local/ssdb/ssdb.conf"]  

