FROM alpine:edge  
  
MAINTAINER daewood <daewood@qq.com>  
  
ENV S6OVERLAY_VERSION=v1.19.1.1 \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=1 \  
LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
TERM=xterm  
  
RUN apk update \  
&& apk upgrade \  
&& apk add curl \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xz -C / \  
&& apk del curl \  
&& rm -rf /var/cache/apk/* /src  
  
COPY rootfs/ /  
  
ENTRYPOINT ["/init"]  
  

