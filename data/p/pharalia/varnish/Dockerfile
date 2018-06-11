FROM debian:jessie  
  
MAINTAINER Michael Oldroyd <docker@michaeloldroyd.co.uk>  
  
RUN apt-get update && apt-get install -y ca-certificates curl apt-transport-
https --no-install-recommends && \  
bash -c "curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -" && \  
bash -c 'echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1"
>> /etc/apt/sources.list.d/varnish-cache.list' && \  
apt-get update && apt-get install -y varnish --no-install-recommends && \  
rm -r /var/lib/apt/lists/*  
  
CMD bash -c \  
"exec varnishd -F \  
-f /etc/varnish/default.vcl \  
-S /etc/varnish/secret \  
-s malloc,64M \  
$VARNISH_PARAMS"  

