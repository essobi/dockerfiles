FROM alpine:3.5  
  
RUN mkdir /sd  
ADD scripts/* /sd/  
RUN chmod +x /sd/hyper-runner.sh \  
&& chmod +x /sd/install_docker.sh \  
&& set -x \  
# Alpine ships with musl instead of glibc (this fixes the symlink)  
&& mkdir /lib64 \  
&& ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \  
&& apk add \--no-cache \--update ca-certificates \  
&& apk add \--virtual .build-dependencies wget \  
&& apk add \--update bash sudo curl \  
# Download latest hyperctl binary from github release  
&& wget -q -O - https://github.com/screwdriver-cd/hyperctl-
image/releases/latest \  
| egrep -o '/screwdriver-cd/hyperctl-
image/releases/download/v[0-9.]*/hyperctl' \  
| wget \--base=http://github.com/ -i - -O hyperctl \  
&& mv hyperctl /usr/bin/hyperctl \  
&& chmod +x /usr/bin/hyperctl \  
&& apk del \--purge .build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/sd/hyper-runner.sh"]  

