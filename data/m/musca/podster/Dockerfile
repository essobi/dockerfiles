FROM alpine:3.4  
COPY podster /usr/local/bin/podster  
RUN set -x \  
&& apk add --no-cache ca-certificates curl ffmpeg python \  
&& curl -Lo /usr/local/bin/youtube-dl https://yt-
dl.org/downloads/latest/youtube-dl \  
&& chmod a+rx /usr/local/bin/youtube-dl \  
&& chmod a+rx /usr/local/bin/podster \  
&& apk del curl \  
&& mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt  
ENV LC_ALL=C.UTF-8  
ENTRYPOINT ["/usr/local/bin/podster"]  

