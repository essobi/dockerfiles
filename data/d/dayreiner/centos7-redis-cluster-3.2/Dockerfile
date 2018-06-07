FROM centos:latest  
MAINTAINER dayreiner  
  
ENV REDIS_URL=https://github.com/antirez/redis.git \  
REDIS_VERSION=3.2 \  
GOSU_URL=https://github.com/tianon/gosu/releases/download \  
GOSU_VERSION=1.10 \  
SRCDIR=/usr/src/redis \  
BINDIR=/usr/local/bin  
  
# Updates and Install build requirements  
RUN yum clean all && yum makecache fast && yum -y update \  
# Reset yum history so we can rollback the devtools installs / reduce image
size  
&& yum clean all && yum history new \  
&& yum -y install git gcc make glibc-devel git  
  
# Build Redis  
RUN groupadd -r redis && useradd -r -g redis redis \  
&& mkdir -p ${SRCDIR} \  
&& git clone -b ${REDIS_VERSION} "${REDIS_URL}" ${SRCDIR} \  
&& make -C ${SRCDIR} \  
&& make -C ${SRCDIR} install \  
# Add redis-trib for future use, assuming it can work from a container  
&& cp ${SRCDIR}/src/redis-trib.rb ${BINDIR}/redis-trib.rb \  
&& chmod +x ${BINDIR}/redis-trib.rb \  
&& rm -rf ${SRCDIR} \  
&& yum -y history undo 1 && yum clean all \  
&& mkdir /data && chown redis: /data  
  
# Add gosu  
RUN gpg --keyserver na.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o ${BINDIR}/gosu -SL "${GOSU_URL}/${GOSU_VERSION}/gosu-amd64" \  
&& curl -o ${BINDIR}/gosu.asc -SL "${GOSU_URL}/${GOSU_VERSION}/gosu-amd64.asc"
\  
&& gpg --verify ${BINDIR}/gosu.asc \  
&& rm ${BINDIR}/gosu.asc \  
&& rm -rf /root/.gnupg/ \  
&& chmod +x ${BINDIR}/gosu  
  
VOLUME /data  
WORKDIR /data  
  
COPY redis.conf /etc/redis.conf  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 6379 16379  
CMD [ "redis-server", "/etc/redis.conf" ]  

