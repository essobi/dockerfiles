# kentwait/alpine-base:latest  
FROM gliderlabs/alpine:3.4  
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV S6_OVERLAY_VERSION 1.18.1.5  
RUN apk update && apk upgrade \  
&& apk add --no-cache bash \  
&& apk add --no-cache --virtual temp-pkgs \  
build-base \  
curl \  
ca-certificates \  
# S6-overlay  
&& curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xvzf - -C / \  
# remove packages and clean up  
&& apk del temp-pkgs \  
&& rm -rf /tmp/* \  
/var/cache/apk/* \  
/root/.wget-hsts  
  
WORKDIR /  

