FROM alpine:3.5  
MAINTAINER Erlend Finvåg <erlend.finvag@gmail.com>  
  
ENV CRON_PATTERN="13 * * * *" \  
USER_ID="1000" GROUP_ID="1000"  
VOLUME /data/html  
VOLUME /data/metadata  
  
# Install reposado  
RUN apk add --no-cache dumb-init dcron curl python && \  
curl -sSL https://github.com/wdas/reposado/tarball/master | tar zx && \  
mv wdas-reposado-* reposado && \  
mkdir -p /data/html /data/metadata && \  
adduser -D reposado && \  
chown -R reposado /data  
  
ENV PATH=/reposado/code:$PATH  
  
COPY preferences.plist /reposado/code  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

