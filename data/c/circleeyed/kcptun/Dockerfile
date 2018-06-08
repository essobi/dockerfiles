FROM alpine:latest as builder  
  
ENV KCPTUN kcptun-linux-amd64  
ENV VERSION 20180316  
RUN apk add --no-cache --update curl  
  
RUN mkdir /root/$KCPTUN \  
&& curl -sSL
https://github.com/xtaci/kcptun/releases/download/v$VERSION/$KCPTUN-$VERSION.tar.gz
\  
| tar -xvzf - -C /root/$KCPTUN \  
&& chmod +x /root/$KCPTUN/*  
  
FROM alpine:latest  
  
LABEL maintainer="cyclops.zhao@protonmail.com"  
  
ENV KCPTUN kcptun-linux-amd64  
  
# add our user and group first to make sure their IDs get assigned  
# consistently, regardless of whatever dependencies get added  
RUN addgroup kcptun \  
&& adduser -g kcptun -G kcptun -D -H kcptun  
  
COPY \--from=builder /root/$KCPTUN/* /usr/local/bin/  
  
RUN apk add --no-cache --update su-exec  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh \  
&& ln -s /usr/local/bin/docker-entrypoint.sh / # backwards compat  
  
EXPOSE 12948 29900  
ENTRYPOINT ["docker-entrypoint.sh"]  

