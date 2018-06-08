FROM alpine:edge  
  
ARG UNISON_VERSION=2.48.4  
RUN apk add --no-cache build-base curl bash inotify-tools && \  
apk add --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ ocaml && \  
curl -L https://github.com/bcpierce00/unison/archive/$UNISON_VERSION.tar.gz |
tar zxv -C /tmp && \  
cd /tmp/unison-${UNISON_VERSION} && \  
sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
src/fsmonitor/linux/inotify_stubs.c && \  
make UISTYLE=text NATIVE=true STATIC=true && \  
cp src/unison src/unison-fsmonitor /usr/local/bin && \  
apk del curl build-base ocaml && \  
apk add --no-cache libgcc libstdc++ && \  
rm -rf /tmp/unison-${UNISON_VERSION} && \  
mkdir -p /home/app/myapp  
  
ENV HOME=/root  
WORKDIR /home/app/myapp  
EXPOSE 12124  
CMD unison -socket 12124  

