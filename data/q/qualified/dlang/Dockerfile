FROM alpine:3.7  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
ARG LDC_VERSION=1.8.0  
RUN set -ex; \  
apk add \--no-cache \  
llvm5 \  
musl-dev \  
gcc \  
curl \  
tzdata \  
openssl \  
xz \  
tar \  
; \  
mkdir -p /opt/ldc; \  
curl -fsSL "https://github.com/ldc-
developers/ldc/releases/download/v${LDC_VERSION}/ldc2-${LDC_VERSION}-alpine-
linux-x86_64.tar.xz" | tar -xJf - -C /opt/ldc \--strip-components=1; \  
chown -R root:root /opt/ldc;  
  
ENV PATH="/opt/ldc/bin:$PATH" \  
LD_LIBRARY_PATH="/opt/ldc/lib:/usr/lib:/lib:$LD_LIBRARY_PATH" \  
LIBRARY_PATH="/opt/ldc/lib:/usr/lib:/lib:$LD_LIBRARY_PATH"  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

