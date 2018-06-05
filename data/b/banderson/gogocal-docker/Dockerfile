FROM alpine  
  
MAINTAINER brendan_anderson@hcpss.org  
  
LABEL vendor=Howard\ County\ Public\ Schools \  
org.hcpss.version="0.2.0" \  
org.hcpss.name="gogocal"  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps wget \  
&& apk --no-cache add ca-certificates \  
&& wget https://github.com/HCPSS/gogocal/releases/download/v0.2.0/gogocal-
linux-amd64 \  
-O /usr/local/bin/gogocal \  
\--no-check-certificate \  
&& chmod u+x /usr/local/bin/gogocal \  
&& mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2 \  
&& apk del .build-deps  
  
CMD ["gogocal", "-k", "/root/key.json"]  

