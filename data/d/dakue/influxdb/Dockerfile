FROM debian:jessie  
MAINTAINER Daniel Kuehne <dkhmailto@googlemail.com>  
  
ENV INFLUXDB_VERSION 0.9.6  
ENV GOSU_VERSION 1.7  
ENV ENVPLATE_VERSION 0.0.8  
ENV TZ Europe/Berlin  
ENV TINI_VERSION 0.8.4  
RUN echo $TZ > /etc/timezone && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure tzdata  
  
RUN set -x && \  
apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends curl
ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN set -x && \  
curl -sSL
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb -o
/tmp/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
rm /tmp/influxdb_${INFLUXDB_VERSION}_amd64.deb  
  
RUN set -x && \  
curl -sSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture)" -o /usr/local/bin/gosu && \  
chmod +x /usr/local/bin/gosu && \  
curl -ssL
"https://github.com/kreuzwerker/envplate/releases/download/v${ENVPLATE_VERSION}/ep-
linux" -o /usr/local/bin/ep && \  
chmod +x /usr/local/bin/ep && \  
ln -s /usr/local/bin/ep /usr/local/bin/envplate && \  
curl -sSL
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static" -o /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
COPY influxdb.conf /etc/influxdb/config.toml  
  
RUN set -x && \  
mkdir -p /var/run/influxdb && \  
chown -R influxdb:influxdb /var/run/influxdb && \  
mkdir -p /var/lib/influxdb && \  
chown -R influxdb:influxdb /var/lib/influxdb  
  
VOLUME /var/lib/influxdb  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
COPY influxdb-start.sh /  
RUN chmod +x /influxdb-start.sh  
  
COPY influxdb-setup.sh /  
RUN chmod +x /influxdb-setup.sh  
  
EXPOSE 2003 4242 8083 8086 8088 25826/udp  
  
ENTRYPOINT ["/usr/local/bin/tini","--","/docker-entrypoint.sh"]  
CMD ["influxdb"]  

