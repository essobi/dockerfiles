FROM alpine  
  
ARG LEDGER_VERSION=next  
  
RUN apk add --no-cache --virtual .build-deps \  
boost boost-iostreams boost-unit_test_framework gmp mpfr3 \  
boost-dev gmp-dev mpfr-dev cmake make g++ wget \  
&& wget -qO- https://github.com/ledger/ledger/archive/$LEDGER_VERSION.tar.gz |
tar xz -C /tmp \  
&& cd /tmp/ledger-$LEDGER_VERSION \  
&& ./acprep update --boost-suffix=-mt --prefix=/usr/local -j2 install \  
&& rm -rf /tmp/ledger-$LEDGER_VERSION \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .php-rundeps $runDeps \  
&& apk del .build-deps  
  
ENTRYPOINT ["ledger"]  
  
CMD ["bal"]  

