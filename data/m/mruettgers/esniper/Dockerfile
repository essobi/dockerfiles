FROM alpine  
MAINTAINER Michael Ruettgers <michael@ruettgers.eu>  
  
ENV ESNIPER_VERSION master  
  
RUN apk add --update build-base curl-dev bash git && \  
rm -rf /var/cache/apk/*  
  
RUN cd /tmp/ && \  
git clone -b ${ESNIPER_VERSION} --depth 1
https://github.com/mruettgers/esniper.git && \  
cd /tmp/esniper && \  
./configure && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf /tmp/esniper  
  
RUN ([ -d /var/lib/esniper ] || mkdir -p /var/lib/esniper) && \  
([ -d /var/lib/esniper/logs ] || mkdir -p /var/lib/esniper/logs) && \  
addgroup esniper && \  
adduser -D -G esniper -h /var/lib/esniper -u 1000 esniper && \  
chown -R esniper:esniper /var/lib/esniper  
  
COPY ./docker/ /docker/  
WORKDIR /var/lib/esniper  
USER esniper  
ENTRYPOINT ["/docker/entrypoint.sh"]

