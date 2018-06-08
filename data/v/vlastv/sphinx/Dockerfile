# Sphinx Search  
#  
# VERSION 0.0.1  
  
FROM alpine  
  
MAINTAINER Vladislav Vlastovskiy <me@vlastv.ru>  
  
ENV SPHINX_VERSION 2.2.11  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
g++ \  
musl-dev \  
mariadb-dev \  
tar \  
make \  
&& mkdir -p /usr/src/sphinx \  
&& cd /usr/src \  
&& wget -O sphinx.tar.gz
"http://sphinxsearch.com/files/sphinx-$SPHINX_VERSION-release.tar.gz" \  
&& tar -xzf sphinx.tar.gz -C "/usr/src/sphinx" \--strip-components=1 \  
&& rm sphinx.tar.gz \  
&& cd /usr/src/sphinx \  
&& sed -i '44 i\\#undef PAGE_SIZE' src/sphinx.cpp \  
&& ./configure \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
&& cd .. \  
&& rm -rf /usr/src/sphinx \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .sphinx-rundeps $runDeps \  
\  
&& apk del .build-deps  
  
CMD ["searchd", "--nodetach"]  

