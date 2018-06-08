# Copyright 2016 Valentine C  
FROM justcontainers/base-alpine  
  
MAINTAINER Valentine C  
  
RUN apk add --update \  
py-pip \  
ca-certificates \  
&& pip install \  
sopel \  
ipython \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
VOLUME ["/sopel"]  
  
COPY 01-sopel etc/fix-attrs.d/01-sopel  
COPY sopel-run.sh etc/services.d/sopel/run  
  
ENTRYPOINT ["/init"]

