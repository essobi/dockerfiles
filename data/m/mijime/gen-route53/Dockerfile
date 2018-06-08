FROM python:alpine  
  
RUN pip install --upgrade awscli  
  
ENV DOCKER_GEN_VERSION=0.7.0 \  
DOCKER_GEN_OS=alpine-linux-amd64  
  
RUN apk add --update curl ca-certificates && \  
curl -OL https://github.com/jwilder/docker-
gen/releases/download/${DOCKER_GEN_VERSION}/docker-
gen-${DOCKER_GEN_OS}-${DOCKER_GEN_VERSION}.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-
gen-${DOCKER_GEN_OS}-${DOCKER_GEN_VERSION}.tar.gz \  
&& rm /docker-gen-${DOCKER_GEN_OS}-${DOCKER_GEN_VERSION}.tar.gz \  
&& apk del  
  
ENV DOCKER_HOST=unix:///tmp/docker.sock \  
HOST_ZONE_ID=<SET_YOUR_HOST_ZONE_ID> \  
HOST_ZONE_DOMAIN= \  
HOST_TYPE=CNAME \  
HOST_NAME=  
  
COPY route53.json.tmpl /etc/route53.json.tmpl  
  
COPY update-route53.sh /usr/local/bin/update-route53.sh  
RUN chmod +x /usr/local/bin/update-route53.sh  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["docker-gen", "-watch", "-only-exposed", "-notify", "update-route53.sh",
"/etc/route53.json.tmpl", "/etc/route53.json"]  

