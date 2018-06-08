FROM alpine:latest  
  
# Install kubectl & gettext(envsubst)  
  
RUN apk add --update ca-certificates gettext \  
&& apk add --update -t deps curl \  
&& curl -L -o /usr/local/bin/kubectl
https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/latest.txt)/bin/linux/amd64/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/* \  
&& kubectl version --client \  
&& envsubst --version

