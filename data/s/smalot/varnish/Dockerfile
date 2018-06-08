FROM debian:latest  
MAINTAINER "Sebastien Malot" <sebastien@malot.fr>  
  
RUN apt-get update && apt-get install -y curl python --no-install-recommends
&& rm -r /var/lib/apt/lists/*  
RUN curl http://repo.varnish-cache.org/GPG-key.txt | apt-key add --  
RUN echo "deb http://repo.varnish-cache.org/debian/ jessie varnish-3.0" >>
/etc/apt/sources.list.d/varnish-cache.list  
RUN apt-get update && apt-get install -y varnish --no-install-recommends && rm
-r /var/lib/apt/lists/*  
RUN mkdir -p /etc/varnish/conf.d/  
  
COPY assemble_vcls.py /assemble_vcls.py  
COPY add_backends.py /add_backends.py  
COPY start.sh /usr/bin/start  
COPY track_hosts.sh /usr/bin/track_hosts  
COPY reload.sh /usr/bin/reload  
COPY default.vcl /etc/varnish/default.vcl  
  
CMD ["start"]  

