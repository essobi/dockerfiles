FROM frolvlad/alpine-glibc:alpine-3.3  
MAINTAINER WOW! Group Development  
  
RUN apk -Uv add curl docker coreutils ca-certificates \  
&& curl -sSL -o /tmp/nomad.zip
https://releases.hashicorp.com/nomad/0.4.1/nomad_0.4.1_linux_amd64.zip \  
&& unzip -d /bin/ /tmp/nomad.zip \  
&& apk --purge -v del curl \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
ENTRYPOINT ["/bin/nomad"]  

