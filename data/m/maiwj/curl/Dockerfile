FROM alpine:3.6  
  
MAINTAINER Frank Mai <frank@rancher.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL \  
io.github.thxcode.build-date=$BUILD_DATE \  
io.github.thxcode.name="curl" \  
io.github.thxcode.description="CURL supports by Alpine in a docker container."
\  
io.github.thxcode.url="https://github.com/thxcode/curl" \  
io.github.thxcode.vcs-type="Git" \  
io.github.thxcode.vcs-ref=$VCS_REF \  
io.github.thxcode.vcs-url="https://github.com/thxcode/curl.git" \  
io.github.thxcode.vendor="Rancher Labs, Inc" \  
io.github.thxcode.version=$VERSION \  
io.github.thxcode.schema-version="1.0" \  
io.github.thxcode.license="MIT" \  
io.github.thxcode.docker.dockerfile="/Dockerfile"  
  
ENV CURL_VERSION 7.56.1-r0  
  
RUN apk add --update --no-cache \  
dumb-init bash sudo \  
openssl jq \  
"curl=${CURL_VERSION}" \  
&& rm -fr /var/cache/apk/*  
  
CMD ["/bin/bash"]

