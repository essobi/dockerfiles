FROM jalaziz/base:alpine  
  
RUN apk add --update go g++ \  
&& rm -rf /var/cache/apk/*  
  
RUN wget -qO- https://github.com/chrislusf/teeproxy/archive/master.tar.gz |
tar -xzC /tmp \  
&& cd /tmp/teeproxy-master && go build \  
&& mv teeproxy-master /usr/local/bin/teeproxy \  
&& rm -rf /tmp/*  
  
ENTRYPOINT [ "/usr/local/bin/teeproxy" ]

