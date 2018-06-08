FROM ubuntu:xenial  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="GPLv3" \  
"Version"="0.0.1"  
  
ARG S6_VERSION="1.19.1.1"  
ARG CONFD_VERSION="0.11.0"  
ENV DEBIAN_FRONTEND=noninteractive \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=1 \  
TERM=xterm  
  
COPY rootfs /  
  
# Install essentials.  
RUN apt-install \  
curl \  
ca-certificates \  
netcat \  
&& \  
curl -L https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
| \  
tar -xzf - -C / && \  
curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 && \  
chmod a+x /usr/local/bin/confd && \  
cleanup  
  
# Start s6  
ENTRYPOINT [ "/init" ]

