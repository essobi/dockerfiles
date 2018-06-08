FROM alpine:latest  
  
ENV DOCKERIZE_VERSION=0.3.0  
WORKDIR /monorail  
  
RUN apk --no-cache add openssl \  
&& wget
http://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& rm dockerize-alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& mkdir -p /opt/monorail/static/http  
  
COPY config.json.tmpl index.html /monorail/  
  
CMD ["dockerize", \  
"-template", "/monorail/config.json.tmpl:/opt/monorail/config.json", \  
"-template", "/monorail/index.html:/opt/monorail/static/http/index.html", \  
"sh", "-c", "while sleep 3600; do :; done"]  

