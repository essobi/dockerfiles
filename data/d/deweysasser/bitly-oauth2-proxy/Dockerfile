FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
RUN apt-get update && apt-get -y install curl  
  
ARG VERSION=2.2  
ARG
URL=https://github.com/bitly/oauth2_proxy/releases/download/v${VERSION}/oauth2_proxy-$VERSION.0.linux-
amd64.go1.8.1.tar.gz  
  
RUN curl -L $URL | tar \--strip-components=1 -xvz  
  
ENTRYPOINT ["/oauth2_proxy"]  

