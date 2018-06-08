FROM ruby:alpine  
  
ENV MAILCATCHER_VERSION 0.6.5  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
sqlite-dev \  
&& gem install mailcatcher -v ${MAILCATCHER_VERSION} \  
&& rm -rf /usr/local/bundle/cache \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .mailcatcher-rundeps $runDeps \  
&& apk del --no-cache .build-deps  
  
COPY patches /tmp/patches  
RUN cd /usr/local/bundle/gems/mailcatcher-* \  
&& for diff in /tmp/patches/*.diff; do patch -p1 < $diff; done \  
&& rm -rf /tmp/patches  
  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 1025 1080  
CMD ["mailcatcher", "--foreground", "--no-quit", "--ip", "0.0.0.0"]  

