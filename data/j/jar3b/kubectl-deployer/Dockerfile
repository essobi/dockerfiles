FROM alpine:3.5  
  
MAINTAINER Sergii Nuzhdin <ipaq.lw@gmail.com@gmail.com>  
MAINTAINER Jack Stdin <hellotan@live.ru>  
  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& apk add --update gettext \  
&& curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl
\  
&& chmod +x /usr/local/bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  

