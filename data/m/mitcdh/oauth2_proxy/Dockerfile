FROM alpine:latest  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
ENV OAUTH2_PROXY_RELEASE=2.2 OAUTH2_PROXY_VERSION=2.2.0 GO_VERSION=go1.8.1  
RUN apk --update add curl \  
&& curl -sL -o oauth2_proxy.tar.gz \  
"https://github.com/bitly/oauth2_proxy/releases/download/v${OAUTH2_PROXY_RELEASE}/oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-
amd64.${GO_VERSION}.tar.gz" \  
&& tar xzvf oauth2_proxy.tar.gz \  
&& mv oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-
amd64.${GO_VERSION}/oauth2_proxy /usr/local/bin/ \  
&& chmod +x /usr/local/bin/oauth2_proxy \  
&& rm -r oauth2_proxy* \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /config  
ENTRYPOINT ["oauth2_proxy"]  
CMD ["-config", "/config/oauth2_proxy.cfg"]  

