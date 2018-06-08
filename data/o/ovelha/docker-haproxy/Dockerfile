FROM alpine  
MAINTAINER Fernando Ribeiro <fernando@finer.com.br>  
  
RUN apk update \  
&& apk add haproxy ca-certificates curl openssl rsyslog bash  
  
ENV DOCKER_GEN_VERSION 0.7.3  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
WORKDIR /app/  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
ADD template/haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD template/rsyslog.conf /etc/rsyslog.conf  
ADD template/run.sh /app/run.sh  
ADD template/reload.sh /usr/bin/reload-haproxy  
ADD template/haproxy.tpl /app/haproxy.tpl  
  
RUN chmod +x /app/run.sh  
RUN chmod +x /usr/bin/reload-haproxy  
ENTRYPOINT ["/app/run.sh"]

