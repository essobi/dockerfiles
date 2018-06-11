FROM alpine:edge  
  
ENV TZ="UTC" \  
LANG="C.UTF-8" \  
UNISON_SOURCE="/source" \  
UNISON_DIR="/data" \  
UNISON_UID="1000" \  
UNISON_USER="docker" \  
UNISON_GID="1000" \  
UNISON_GROUP="docker" \  
UNISON_VERSION="2.48.4"  
RUN apk add --no-cache build-base curl su-exec inotify-tools tzdata \  
&& apk add --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ ocaml \  
&& curl -L https://github.com/bcpierce00/unison/archive/$UNISON_VERSION.tar.gz
| tar zxv -C /tmp \  
&& cd /tmp/unison-${UNISON_VERSION} \  
&& sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
src/fsmonitor/linux/inotify_stubs.c \  
&& make UISTYLE=text NATIVE=true STATIC=true \  
&& cp src/unison src/unison-fsmonitor /usr/local/bin \  
&& apk del curl build-base ocaml \  
&& apk add --no-cache libgcc libstdc++ \  
&& rm -rf /tmp/unison-${UNISON_VERSION}  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD su-exec $UNISON_USER:$UNISON_GROUP unison $UNISON_SOURCE $UNISON_DIR -auto
-batch -repeat watch  

