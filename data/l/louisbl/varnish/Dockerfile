FROM debian:jessie  
MAINTAINER louisbl <louis@beltramo.me>  
  
RUN apt-get update && apt-get install -y curl apt-transport-https \  
&& curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - \  
&& echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list \  
&& apt-get update \  
&& apt-get install -y varnish \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD default.vcl /etc/varnish/default.vcl  
  
EXPOSE 80  
CMD varnishd -F -b $BACKEND_PORT_80_TCP_ADDR:$BACKEND_PORT_80_TCP_PORT  

