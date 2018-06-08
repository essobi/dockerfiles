FROM alpine:3.5  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="GPLv3" \  
"Version"="0.0.1"  
  
ARG S6_VERSION="1.19.1.1"  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
PYTHONPATH=/usr/lib/python2.7/site-packages  
  
RUN apk --update add ca-certificates curl docker libssh2 openssl py-pip python
&& \  
pip install --no-cache-dir --upgrade pip && \  
pip install --no-cache-dir docker-compose && \  
curl -L https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
| \  
tar -xzf - -C / && \  
rm -rf /var/cache/apk/* \  
/root/.cache/* \  
/tmp/*  
  
ENTRYPOINT [ "/init" ]  
EXPOSE 8000  
WORKDIR /root  
COPY rootfs /  

