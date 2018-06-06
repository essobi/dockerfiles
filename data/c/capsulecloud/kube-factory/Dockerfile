FROM node:alpine  
  
LABEL maintainer Kazuhito Yamazawa <yamazawa@supersoftware.co.jp>  
  
ARG SCALEWAY_VERSION="v1.16"  
RUN apk --update add ca-certificates git openssh curl jq bash-completion ruby
ruby-rake ruby-io-console ruby-bundler docker make bash bind-tools && \  
mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
&& \  
echo "source /etc/profile.d/bash_completion.sh" >> ~/.bashrc && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
RUN npm install -g cloudflare-cli  
  
RUN curl -LO https://github.com/scaleway/scaleway-
cli/releases/download/$SCALEWAY_VERSION/scw-linux-amd64 && \  
chmod +x ./scw-linux-amd64 && \  
mv ./scw-linux-amd64 /usr/local/bin/scw  
  
COPY . /usr/local/src/kube-factory/  
WORKDIR /usr/local/src/kube-factory  
  
ENTRYPOINT ["./docker-entrypoint.sh"]

