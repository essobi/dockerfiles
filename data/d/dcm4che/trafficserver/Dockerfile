FROM debian:jessie  
  
ENV TS_VERSION=7.0.0 \  
TS_HOME=/opt/ats  
  
# explicitly set user/group IDs  
RUN groupadd -r tserver --gid=1030 && useradd -r -g tserver --uid=1030 tserver  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get -y install gcc bzip2 libc6-dev linux-libc-dev make curl
libncursesw5-dev libssl-dev zlib1g-dev libpcre3-dev \  
perl libxml2-dev libcap-dev tcl8.6-dev libhwloc-dev libgeoip-dev
libmysqlclient-dev libkyotocabinet-dev libreadline-dev \  
&& apt-get clean \  
&& cd /usr/src \  
&& curl -L http://www-
eu.apache.org/dist/trafficserver/trafficserver-${TS_VERSION}.tar.bz2 | tar xj
\  
&& cd trafficserver-${TS_VERSION} \  
&& ./configure --prefix=${TS_HOME} \--with-user=tserver --enable-experimental-
plugins --disable-hwloc && make && make install \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/src/trafficserver-${TS_VERSION} \  
&& mkdir /docker-entrypoint.d && mv $TS_HOME/etc /docker-entrypoint.d  
  
# Default configuration: can be overridden at the docker command line  
ENV TS_MAP_TARGET=http://localhost:8080 \  
TS_MAP_REPLACEMENT=http://dcm4chee-arc:8080 \  
TS_STORAGE="var/trafficserver 256M" \  
TS_WHEN_TO_REVALIDATE=2  
ENV PATH $TS_HOME/bin:$PATH  
  
VOLUME $TS_HOME/var  
  
# Expose the ports we're interested in  
EXPOSE 8080  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["traffic_cop", "-o"]  

