FROM alpine  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
ENV KAFKA_CONNECT_UI_VER 0.9.2  
# Install needed packages  
RUN apk update; \  
apk add -u python py-pip git wget nodejs-npm bash  
RUN pip install supervisor  
  
WORKDIR /  
  
RUN wget
"https://github.com/mholt/caddy/releases/download/v0.9.5/caddy_linux_amd64.tar.gz"
-O /caddy.tgz; \  
mkdir /caddy; \  
tar xzf /caddy.tgz -C /caddy; \  
mv /caddy/caddy_linux_amd64 /caddy/caddy; \  
rm -f /caddy.tgz  
  
RUN npm install -g bower  
RUN adduser parrot -D -h /schema-registry-ui; \  
chown parrot:parrot /schema-registry-ui  
  
USER parrot  
  
WORKDIR /schema-registry-ui  
  
ADD src src  
ADD *.* ./  
RUN npm install  
RUN npm run-script build-prod  
  
WORKDIR /  
  
USER root  
  
ADD docker/etc/ /etc/  
ADD docker/Caddyfile /caddy/  
ADD docker/start-schema-registry-ui.sh /  
ADD docker/supervisord-bootstrap.sh /  
RUN chmod o=rx /*.sh; \  
chmod o=rxw /caddy  
RUN chown parrot:parrot /schema-registry-ui/logs  
  
USER parrot  
  
EXPOSE 8000  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

