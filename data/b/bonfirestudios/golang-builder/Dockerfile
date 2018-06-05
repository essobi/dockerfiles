FROM golang:1.7-alpine  
RUN apk add -U git \  
&& go get -u github.com/aws/aws-sdk-go/aws/... \  
&& go get -u github.com/aws/aws-sdk-go/service/... \  
\  
&& apk add -U --virtual .curl curl \  
&& curl -LO https://github.com/github/git-lfs/releases/download/v1.4.4/git-
lfs-linux-amd64-1.4.4.tar.gz \  
&& apk del .curl \  
&& tar xf git-lfs-linux-amd64-1.4.4.tar.gz \  
&& mv git-lfs-1.4.4/git-lfs /usr/bin \  
&& rm -rf git-lfs-1.4.4 \  
&& rm git-lfs-linux-amd64-1.4.4.tar.gz \  
&& git lfs install  

