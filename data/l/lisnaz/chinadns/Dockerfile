#  
# Dockerfile for chinadns  
#  
FROM alpine  
MAINTAINER Vincent.Gu <g@v-io.co>  
  
ENV PORT 53  
ENV APP_DIR /srv/chinadns  
ENV CDNS_VER 1.3.3  
ENV CDNS_URL https://github.com/v-gu/ChinaDNS/archive/v${CDNS_VER}.tar.gz  
ENV CDNS_DIR $APP_DIR/ChinaDNS-$CDNS_VER  
ENV CHNROUTE_FILE $APP_DIR/chnroute.txt  
ENV CHINA_DNS 223.5.5.5  
ENV OFFSHORE_DNS 8.8.8.8  
EXPOSE $PORT/udp  
  
WORKDIR $APP_DIR  
  
# build software stack  
ENV BUILD_DEP musl-dev automake autoconf gcc gawk make libtool curl  
RUN set -ex \  
&& apk --update --no-cache add $BUILD_DEP $DEP \  
&& curl -sSL "$CDNS_URL" | tar xz -C $APP_DIR \  
&& curl 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest' \  
| grep ipv4 \  
| grep CN \  
| awk -F\| '{printf("%s/%d\n", $4, 32-log($5)/log(2))}' >>
$APP_DIR/chnroute.txt \  
&& cd $CDNS_DIR \  
&& ./autogen.sh \  
&& ./configure \  
&& make install \  
&& cd $APP_DIR \  
&& rm -rf $CDNS_DIR \  
&& apk del --purge $BUILD_DEP \  
&& rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

