FROM postgres:10-alpine  
MAINTAINER coolyaolei@sina.com  
  
ENV CSTORE_VER 1.6.0  
USER root  
WORKDIR /root  
  
# Change mirror site For China  
#RUN echo 'https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/main' >
/etc/apk/repositories && \  
# echo 'https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/community' >>
/etc/apk/repositories  
RUN apk --no-cache add alpine-sdk protobuf-c-dev && \  
curl -SL https://github.com/citusdata/cstore_fdw/archive/v${CSTORE_VER}.tar.gz
|tar zxC . && \  
cd cstore_fdw-${CSTORE_VER} && \  
make && \  
make install && \  
cd /root && rm -rf cstore_fdw-${CSTORE_VER} && \  
apk del alpine-sdk && \  
rm -rf /var/cache/apk/* && \  
echo -e 'echo "shared_preload_libraries = 'cstore_fdw'" >>
${PGDATA}/postgresql.conf' > /docker-entrypoint-initdb.d/cstore_fdw.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

