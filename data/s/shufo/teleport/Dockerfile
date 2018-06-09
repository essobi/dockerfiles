FROM alpine:3.5  
MAINTAINER shufo  
  
ENV TELEPORT_VERSION 2.0.5  
ENV TELEPORT_ROLES auth,proxy,node  
  
  
ENV TELEPORT_NODENAME localhost  
  
RUN apk add --update --no-cache make ca-certificates curl \  
&& update-ca-certificates \  
&& curl -L
https://github.com/gravitational/teleport/releases/download/v${TELEPORT_VERSION}/teleport-v${TELEPORT_VERSION}-linux-
amd64-bin.tar.gz | tar xz -C /tmp \  
&& make -C /tmp/teleport install \  
&& mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2 \  
&& rm -fR /tmp/*  
  
WORKDIR /var/lib/teleport  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  
  
EXPOSE 3022 3023 3024 3025 3080  

