FROM alpine:latest  
  
ARG RC_VERSION="v0.12.5"  
ENV RC_PLATFORM="linux"  
ENV RC_ARCH="amd64"  
ENV RC_EXT="tar.gz"  
RUN apk add --no-cache -q curl  
  
RUN curl -ss -L -o "/tmp/rancher-
compose-${RC_PLATFORM}-${RC_ARCH}-${RC_VERSION}.${RC_EXT}" \  
"https://github.com/rancher/rancher-
compose/releases/download/${RC_VERSION}/rancher-
compose-${RC_PLATFORM}-${RC_ARCH}-${RC_VERSION}.${RC_EXT}"  
  
RUN cd /tmp && \  
tar -zxf rancher-compose-${RC_PLATFORM}-${RC_ARCH}-${RC_VERSION}.${RC_EXT} &&
\  
mv rancher-compose-${RC_VERSION}/rancher-compose /usr/local/bin/rancher-
compose && \  
rm -rf /tmp/*  

