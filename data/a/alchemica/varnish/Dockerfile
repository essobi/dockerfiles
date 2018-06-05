FROM alpine:latest  
  
ENV VARNISH_HOST web  
# ENV VARNISH_TEMPLATE magento  
  
RUN set -ex \  
&& ( \  
apk update \  
&& apk upgrade \  
&& apk add varnish \  
) \  
&& ( \  
apk add \  
\--no-cache \  
git \  
make \  
automake \  
varnish-dev \  
libtool \  
m4 \  
autoconf \  
geoip-dev \  
python \  
py-docutils \  
&& git clone -b master https://github.com/varnish/libvmod-geoip.git
/tmp/libvmod-geoip \  
&& cd /tmp/libvmod-geoip \  
# && git reset --hard b4d72ecc23895d4a0e9b28655093861f0c85cb66 \  
&& ./autogen.sh \  
&& ./configure \  
&& make install \  
&& rm -rf /tmp/libvmod-geoip \  
) \  
&& ( \  
cd /usr/share/GeoIP/ \  
wget -O GeoIP.dat.gz
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
\  
gunzip GeoIP.dat.gz \  
)  
  
ADD etc/*.vcl /etc/varnish/  
ADD bin/* /usr/local/bin/  
  
ENTRYPOINT ["/usr/local/bin/docker-environment"]  
# CMD ["varnishd", "-p", "default_ttl=3600", "-p", "default_grace=3600", "-p",
"feature=+esi_ignore_https", "-p", "feature=+esi_disable_xml_check", "-f",
"/etc/varnish/magento.vcl"]  
# varnishd -p default_ttl=3600 -p default_grace=3600 -p
feature=+esi_ignore_https -p feature=+esi_disable_xml_check

