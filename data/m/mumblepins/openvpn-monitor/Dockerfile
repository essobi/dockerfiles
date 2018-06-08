FROM python:3-alpine3.6  
# ENV VERSION=c70d40167a41f63f396545bc87bf6e2b7dbd496e  
ENV MONITOR_VERSION=master \  
CONFD_VERSION=0.14.0  
RUN set -ex; \  
apk add --no-cache \  
geoip \  
;\  
apk add --no-cache --virtual .build-dependencies \  
gcc \  
linux-headers \  
geoip-dev \  
musl-dev \  
openssl \  
tar \  
curl \  
;\  
curl -sSL \  
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
> /usr/bin/confd; \  
chmod a+x /usr/bin/confd; \  
pip install --no-cache-dir gunicorn; \  
mkdir /openvpn-monitor; \  
curl -sSL https://github.com/furlongm/openvpn-
monitor/archive/${MONITOR_VERSION}.tar.gz \  
| tar -C /openvpn-monitor --strip-components=1 -zxvf - ; \  
pip install --no-cache-dir /openvpn-monitor; \  
mkdir -p /usr/share/GeoIP/; \  
cd /usr/share/GeoIP/ ; \  
curl -sSL
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \  
| gunzip \  
> GeoIPCity.dat; \  
apk del --no-cache .build-dependencies  
  
COPY confd /etc/confd  
COPY entrypoint.sh /  
  
WORKDIR /openvpn-monitor  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["gunicorn", "openvpn-monitor", "--bind", "0.0.0.0:80"]  

