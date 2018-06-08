FROM debian:stable  
MAINTAINER Mildred Ki'Lya  
  
RUN set -e; \  
export DEBIAN_FRONTEND=noninteractive; \  
apt-get update; \  
apt-get -y install curl;  
  
RUN set -e; \  
export DEBIAN_FRONTEND=noninteractive; \  
curl http://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add -; \  
echo "deb http://repo.varnish-cache.org/debian/ wheezy varnish-4.0 >
/etc/apt/sources.list.d/varnish.list"  
apt-get update;  
  
RUN set -e; \  
export DEBIAN_FRONTEND=noninteractive; \  
apt-get install -y varnish vim nano;  
  
RUN mkdir -p /etc/varnish;  
  
VOLUME /etc/varnish  
VOLUME /var/lib/varnish  
  
EXPOSE 80  
  
CMD touch /etc/varnish/default.vcl; \  
cp /etc/varnish/default.vcl /etc/varnish/default.subst.vcl; \  
env | while read envline; do \  
k=${envline%%=*}; \  
v=${envline#*=}; \  
sed -i "s|%${k}%|${v}|g" /etc/varnish/default.subst.vcl; \  
done; \  
varnishlog -D; \  
exec varnishd -F -f /etc/varnish/default.subst.vcl -s malloc,100M -a
0.0.0.0:80  
  

