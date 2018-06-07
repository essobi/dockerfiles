FROM alpine:latest  
  
LABEL maintainer "Viktor Adam <rycus86@gmail.com>"  
  
ARG ARCH=amd64  
ARG VERSION=0.14.0  
RUN apk --no-cache add --virtual build-dependencies wget ca-certificates \  
&& mkdir -p /tmp/install /tmp/dist \  
&& wget -O /tmp/install/node_exporter.tar.gz
https://github.com/prometheus/node_exporter/releases/download/v$VERSION/node_exporter-$VERSION.linux-$ARCH.tar.gz
\  
&& apk del build-dependencies \  
&& apk add --no-cache libc6-compat \  
&& cd /tmp/install \  
&& tar --strip-components=1 -xzf node_exporter.tar.gz \  
&& mv node_exporter /bin/node_exporter \  
&& rm -rf /tmp/install  
  
EXPOSE 9100  
ENTRYPOINT [ "/bin/node_exporter" ]  

