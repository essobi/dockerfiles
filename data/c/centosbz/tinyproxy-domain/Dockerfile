FROM debian:jessie  
LABEL maintainer "admin@centos.bz"  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install tinyproxy \  
&& mkdir -p /var/run/tinyproxy/ \  
&& chown nobody /var/run/tinyproxy/ \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN sed -i 's/^#FilterDefaultDeny .*/FilterDefaultDeny yes/'
/etc/tinyproxy.conf \  
&& sed -i 's|^#Filter .*|Filter "/etc/filter"|' /etc/tinyproxy.conf \  
&& sed -i 's|^Allow 127.0.0.1|#Allow 127.0.0.1|' /etc/tinyproxy.conf \  
&& echo
"github.com\namazonaws.com\nquay.io\ngcr.io\ncloud.google.com\nwordpress.org\n"
> /etc/filter  
  
ENTRYPOINT ["tinyproxy"]  
CMD ["-d"]

