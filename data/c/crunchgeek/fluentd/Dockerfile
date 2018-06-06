FROM fluent/fluentd:v0.12-debian-onbuild  
  
MAINTAINER Mark Hilton <nerd305@gmail.com>  
  
USER root  
  
RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps  
  
RUN apt-get install -y curl gzip libgeoip-dev libmaxminddb-dev  
  
RUN gem sources  
  
RUN gem install \  
fluent-plugin-grep \  
fluent-plugin-parser \  
fluent-plugin-bigquery \  
fluent-plugin-geoip \  
fluent-plugin-ua-parser \  
fluent-plugin-multi-format-parser \  
bigdecimal  
  
# this removes GeoIP db, so we download fresh after  
RUN gem sources --clear-all \  
&& SUDO_FORCE_REMOVE=yes \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
RUN mkdir -p /usr/share/GeoIP && cd /usr/share/GeoIP/ && \  
rm -f GeoIP.dat GeoIPv6.dat && \  
curl -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \  
curl -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
&& \  
gzip -d *  

