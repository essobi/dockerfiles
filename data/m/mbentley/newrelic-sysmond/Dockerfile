FROM debian:jessie  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN (apt-get update &&\  
apt-get install -y wget &&\  
echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list &&\  
wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add \- &&\  
apt-get update &&\  
apt-get install -y newrelic-sysmond &&\  
apt-get purge -y wget &&\  
rm -rf /var/lib/apt/lists/*)  
  
CMD nrsysmond-config --set license_key=$NEW_RELIC_LICENSE_KEY && nrsysmond -c
/etc/newrelic/nrsysmond.cfg -l /dev/stdout -f  

