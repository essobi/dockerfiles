FROM alpine:3.7  
  
ENTRYPOINT ["/usr/bin/crystal"]  
  
RUN wget
http://public.portalier.com/alpine/julien%40portalier.com-56dab02e.rsa.pub -O
/etc/apk/keys/julien@portalier.com-56dab02e.rsa.pub \  
&& echo http://public.portalier.com/alpine/testing >> /etc/apk/repositories  
  
ENV CRYSTAL_VERSION 0.23.1  
  
RUN apk update \  
&& apk add crystal=${CRYSTAL_VERSION}-r1 shards openssl-dev gcc \  
&& rm -rf /var/lib/apt/lists/*

