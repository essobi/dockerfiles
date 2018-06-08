FROM i386/alpine:3.7  
  
RUN apk update \  
&& apk add ca-certificates \  
&& apk add curl \  
&& curl -o /usr/local/bin/roer -L
https://github.com/spinnaker/roer/releases/download/v0.9.0/roer-linux-386 \  
&& chmod +x /usr/local/bin/roer \  
&& apk del curl  

