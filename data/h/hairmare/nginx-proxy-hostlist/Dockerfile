FROM alpine  
  
ENV DOCKER_GEN_VERSION=0.7.3  
RUN apk update && apk add openssl \  
&& wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar zxvf docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& mv docker-gen /usr/local/bin/ \  
&& rm -rf docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /usr/local/share/api  
  
COPY templates /etc/docker-gen/templates  
COPY notify.sh /usr/local/bin/notify.sh  
  
VOLUME "/usr/local/share/api"  
  
ENTRYPOINT ["/usr/local/bin/docker-gen"]  
CMD ["-watch", "-notify", "/usr/local/bin/notify.sh", "/etc/docker-
gen/templates/hosts.tmpl", "/usr/local/share/api/index.json"]  

