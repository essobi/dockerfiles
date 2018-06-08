##  
## build  
##  
FROM trevorj/boilerplate:rolling AS builder  
MAINTAINER Trevor Joynson <docker@trevor.joynson.io>  
  
RUN lazy-apt build-essential  
  
COPY src src  
COPY Makefile README.md nyancat.1 ./  
  
ENV CFLAGS="-static -O2"  
ENV CXXFLAGS="${CFLAGS}"  
RUN make -j4 \  
&& mkdir -pv /out \  
&& cp src/nyancat /out/ \  
&& strip /out/nyancat  
  
##  
## fin  
##  
FROM busybox:latest  
MAINTAINER Trevor Joynson <docker@trevor.joynson.io>  
  
COPY \--from=builder /out/nyancat /bin/  
  
ENV CONN_LIMIT=30 CONN_LIMIT_PER_IP=1  
RUN set -xv \  
&& fn=/bin/nyancat-tcpsvd \  
&& echo -e \  
'#!/bin/sh\nexec busybox tcpsvd -c ${CONN_LIMIT:-30} -C
${CONN_LIMIT_PER_IP:-1} -E -l nyan -v 0.0.0.0 42023 nyancat -It' \  
> "$fn" \  
&& chmod +x "$fn"  
  
EXPOSE 42023  
USER nobody  
CMD ["nyancat-tcpsvd"]  

