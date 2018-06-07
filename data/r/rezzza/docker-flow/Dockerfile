FROM alpine:edge  
  
MAINTAINER Sébastien HOUZÉ <sebastien.houze@verylastroom.com>  
  
ENV FLOW_VERSION=0.39.0  
  
COPY flow.patch /tmp/  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add \--no-cache \--virtual .build-deps \  
alpine-sdk \  
ocaml \  
lz4 \  
lz4-dev \  
ocamlbuild \  
libelf \  
libelf-dev \  
ncurses \  
inotify-tools \  
linux-headers \  
bash \  
diffutils \  
&& cd /tmp \  
&& curl -SL https://github.com/facebook/flow/archive/v${FLOW_VERSION}.tar.gz
-o /tmp/flow-${FLOW_VERSION}.tgz \  
&& tar -C /tmp -xzpf /tmp/flow-${FLOW_VERSION}.tgz \  
&& rm /tmp/flow-${FLOW_VERSION}.tgz \  
&& cd /tmp/flow-${FLOW_VERSION} \  
&& cp /tmp/flow.patch . \  
&& git apply flow.patch \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& cp /tmp/flow-${FLOW_VERSION}/bin/flow /usr/local/bin \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--no-cache \--virtual .flow-rundeps $runDeps \  
&& apk del \--no-cache .build-deps \  
&& rm -rf /tmp/*  
  
VOLUME /app  
WORKDIR /app  
  
CMD ["flow", "check"]  

