FROM soulteary/alpine-base:3.4  
MAINTAINER soulteary <soulteary@gmail.com>  
  
ENV HUGO_VERSION 0.17  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit  
  
RUN apk --no-cache --no-progress update && apk add py-pygments && rm -rf
/var/cache/apk/*  
  
#COPY ./hugo_0.16_linux-64bit.tgz /usr/local/  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/bin/ \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz \  
&& mv /usr/local/bin/hugo_0.17_linux_amd64/hugo_0.17_linux_amd64
/usr/local/bin/hugo  
  
EXPOSE 1313  
CMD ["hugo", "version"]

