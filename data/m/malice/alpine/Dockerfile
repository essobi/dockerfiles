FROM alpine:3.7  
LABEL maintainer "https://github.com/blacktop"  
  
RUN apk add --no-cache tini su-exec  
RUN set -x \  
&& echo "===> Add malice user and malware folder..." \  
&& addgroup malice \  
&& adduser -S -G malice malice \  
&& mkdir /malware \  
&& chown -R malice:malice /malware  

