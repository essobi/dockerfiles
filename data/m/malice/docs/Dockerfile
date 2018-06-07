FROM alpine:3.6  
LABEL maintainer "https://github.com/blacktop"  
  
# VOLUME /var/blog /var/_built  
ARG VERSION=0.29  
RUN apk add --no-cache -t .build-deps curl ca-certificates git mercurial \  
&& echo "===> Install Hugo..." \  
&& curl -sSL
https://github.com/gohugoio/hugo/releases/download/v${VERSION}/hugo_${VERSION}_Linux-64bit.tar.gz
\  
| tar -xzf - -C /tmp \  
&& mv /tmp/hugo /usr/bin/hugo \  
&& rm -rf /tmp/* \  
&& apk del --purge .build-deps  
  
WORKDIR /docs  
  
COPY . .  
RUN apk add --no-cache -t .build-deps curl ca-certificates git \  
&& echo "===> Install hugo-material-docs theme..." \  
&& git clone https://github.com/digitalcraftsman/hugo-material-docs.git
themes/hugo-material-docs \  
&& echo "===> Build website..." \  
&& hugo --theme=hugo-material-docs \  
&& rm -rf /docs/themes/hugo-material-docs/exampleSite \  
&& rm -rf /tmp/* /docs/themes/hugo-material-docs/*.md \  
&& rm -rf /tmp/* /docs/themes/hugo-material-docs/.git \  
&& apk del --purge .build-deps  
  
EXPOSE 80 443  
ENTRYPOINT /docs/entrypoint.sh  

