FROM alpine:latest  
MAINTAINER Shintaro Okamura <info@okash1n.com>  
  
# 必要なパッケージ  
RUN apk add --update --no-cache \  
bash \  
ca-certificates \  
curl \  
git  
  
# hugoのインストール  
ARG HUGO_VERSION=0.32.4  
ARG
HUGO_SHA256=004e437e4afa7a3556019b4215767d6823435d9a4c5b6f82715b93ac93bea44f  
  
RUN curl -Ls
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
-o /tmp/hugo.tar.gz \  
&& echo "${HUGO_SHA256} /tmp/hugo.tar.gz" | sha256sum -c - \  
&& tar xf /tmp/hugo.tar.gz -C /tmp \  
&& mv /tmp/hugo /usr/bin/hugo \  
&& rm -rf /tmp/hugo* \  

