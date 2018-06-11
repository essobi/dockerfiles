FROM alpine:edge  
  
ARG UNISON_VERSION=2.48.4  
RUN apk add --no-cache build-base curl bash\  
&& apk add --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ ocaml\  
&& curl -L https://github.com/bcpierce00/unison/archive/$UNISON_VERSION.tar.gz
| tar zxv -C /tmp \  
&& cd /tmp/unison-${UNISON_VERSION} \  
&& sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
src/fsmonitor/linux/inotify_stubs.c \  
&& make UISTYLE=text NATIVE=true STATIC=true \  
&& cp src/unison src/unison-fsmonitor /usr/local/bin \  
&& apk del curl build-base ocaml \  
&& apk add --no-cache libgcc libstdc++ \  
&& rm -rf /tmp/unison-${UNISON_VERSION} \  
&& apk add --no-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ shadow \  
&& apk add --no-cache tzdata  
  
############# ############# #############  
############# SHARED #############  
############# ############# #############  
  
# These can be overridden later  
ENV TZ="America/Colorado" \  
LANG="C.UTF-8" \  
UNISON_DIR="/data" \  
HOME="/root"  
  
  
RUN mkdir -p /docker-entrypoint.d \  
&& mkdir -p /host_sync \  
&& mkdir -p /usr/src \  
&& touch /tmp/unison.log \  
&& chmod u=rw,g=rw,o=rw /tmp/unison.log  
  
  
CMD ["unison", "-numericids", "-repeat", "watch", "-auto", "-batch",
"/host_sync", "/usr/src", "-logfile", "/tmp/unison.log", "-ignore", "Name
{.*,*}.sw[pon]"]  
  
############# ############# #############  
############# /SHARED / #############  
############# ############# #############  
  
VOLUME /host_sync  

