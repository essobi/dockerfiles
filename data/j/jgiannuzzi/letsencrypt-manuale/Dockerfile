FROM python:3-alpine  
  
ENV MANUALE_VERSION 1.1.0  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libffi-dev \  
musl-dev \  
openssl-dev \  
&& pip install --no-cache-dir manuale==${MANUALE_VERSION} \  
&& find /usr/local -depth \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .manuale-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf ~/.cache  
  
RUN mkdir /data  
VOLUME /data  
WORKDIR /data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["manuale"]  

