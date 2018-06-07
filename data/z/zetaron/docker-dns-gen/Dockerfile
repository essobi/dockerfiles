FROM alpine:latest  
MAINTAINER Fabian Stegemann <fst@zetaron.de>  
  
RUN apk --no-cache add \  
dnsmasq \  
openssl  
  
ENV DOCKER_GEN_VERSION 0.7.3  
ENV DOCKER_HOST unix:///var/run/docker.sock  
  
RUN wget -qO- https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz | tar xvz -C /usr/local/bin  
  
ADD config/dnsmasq.tmpl /etc/dnsmasq.tmpl  
ADD dnsmasq-reload /usr/local/bin/dnsmasq-reload  
ADD entrypoint /usr/local/bin/entrypoint  
ADD generate /usr/local/bin/generate  
  
WORKDIR /app/  
  
EXPOSE 53/udp  
  
ENTRYPOINT ["entrypoint"]  
CMD ["generate"]  

