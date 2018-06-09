FROM alpine:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="docker-alpine-tester" \  
org.label-schema.description="Docker Alpine Tester: para realizar pruebas de
red." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/docker-alpine-tester" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --rm -it --name tester -h tester
jorgeandrada/docker-alpine-tester"  
  
RUN apk add --update drill \  
htop \  
bind-tools \  
wget \  
curl \  
nmap \  
mariadb-client \  
vim \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["sleep","9999999"]  

