FROM gliderlabs/logspout:latest  
  
LABEL maintainer "support@logit.io"  
LABEL version="1.0"  
  
RUN apk add -U --virtual build-dependencies curl ca-certificates \  
&& curl https://cdn.logit.io/logit-intermediate.crt -o /usr/local/share/ca-
certificates/logit-intermediate.crt \  
&& update-ca-certificates \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*

