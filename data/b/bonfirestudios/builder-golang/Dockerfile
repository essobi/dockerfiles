FROM golang:1.8-alpine  
RUN apk add -U git \  
&& apk add -U --virtual .curl curl \  
&& curl -LO https://github.com/git-lfs/git-lfs/releases/download/v2.0.2/git-
lfs-linux-amd64-2.0.2.tar.gz \  
&& apk del .curl \  
&& tar xf git-lfs-linux-amd64-2.0.2.tar.gz \  
&& mv git-lfs-2.0.2/git-lfs /usr/bin \  
&& rm -rf git-lfs-2.0.2 \  
&& rm git-lfs-linux-amd64-2.0.2.tar.gz \  
&& git lfs install  

