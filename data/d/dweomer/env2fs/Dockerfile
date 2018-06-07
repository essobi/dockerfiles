FROM alpine:latest  
  
MAINTAINER Jacob Blain Christen <mailto:dweomer5@gmail.com,
https://github.com/dweomer, https://twitter.com/dweomer>  
  
COPY src/main/container/ /  
  
RUN set -x \  
&& chmod -v +x /srv/*.sh \  
&& apk add --update \  
bash \  
ruby \  
&& rm -rf \  
/tmp/* \  
/var/cache/apk \  
/var/tmp/*  
  
ENTRYPOINT ["/srv/env2fs.sh"]  

