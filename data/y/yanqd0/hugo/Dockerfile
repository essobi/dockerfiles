FROM alpine:3.7  
MAINTAINER Yan QiDong <yanqd0@outlook.com>  
  
ENV HUGO_VERSION=0.40.3 \  
HUGO_USER=hugo \  
HUGO_SITE=/srv/hugo  
  
RUN apk --no-cache add \  
curl \  
git \  
&& curl -SL
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
-o /tmp/hugo.tar.gz \  
&& tar -xzf /tmp/hugo.tar.gz -C /tmp \  
&& apk del curl \  
&& mv /tmp/hugo /usr/local/bin/ \  
&& mkdir -p ${HUGO_SITE} \  
&& addgroup ${HUGO_USER} \  
&& adduser -G ${HUGO_USER} -D ${HUGO_USER} \  
&& chown -R ${HUGO_USER}:${HUGO_USER} ${HUGO_SITE} \  
&& rm -rf /tmp/*  
  
USER ${HUGO_USER}  
  
WORKDIR ${HUGO_SITE}  
  
VOLUME ${HUGO_SITE}  
  
EXPOSE 1313  
CMD hugo server --bind 0.0.0.0 \  
\--navigateToChanged \  
\--templateMetrics \  
\--buildDrafts  

