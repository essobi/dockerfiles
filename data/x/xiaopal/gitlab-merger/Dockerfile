FROM alpine:3.7  
  
RUN export WEBHOOK_RELEASE=2.6.8 GOPATH=/build && \  
apk add \--no-cache -t build-webhook go libc-dev && \  
mkdir -p $GOPATH/src/github.com/adnanh && cd $GOPATH && \  
wget -O webhook-$WEBHOOK_RELEASE.tar.gz
https://github.com/adnanh/webhook/archive/$WEBHOOK_RELEASE.tar.gz && \  
tar -zxf webhook-$WEBHOOK_RELEASE.tar.gz && \  
mv webhook-$WEBHOOK_RELEASE src/github.com/adnanh/webhook && \  
cd src/github.com/adnanh/webhook && \  
go get -d && go build -o /usr/bin/webhook && \  
apk del --purge build-webhook && cd / && rm -fr $GOPATH  
  
RUN apk add \--no-cache bash curl openssl nginx findutils \  
&& curl 'http://npc.nos-eastchina1.126.net/dl/dumb-init_1.2.0_amd64.tar.gz' |
tar -zx -C /usr/bin \  
&& curl 'http://npc.nos-eastchina1.126.net/dl/jq_1.5_linux_amd64.tar.gz' | tar
-zx -C /usr/bin  
  
ADD nginx.conf webhooks.yml run.sh merger.sh /  
RUN chmod a+x /run.sh /merger.sh && \  
ln -sf /merger.sh /usr/bin/secret && \  
ln -sf /merger.sh /usr/bin/api && \  
ln -sf /merger.sh /usr/bin/setup  
  
ENV GITLAB_ENDPOINT= GITLAB_API_TOKEN= \  
GIT_AUTO_MERGE= GIT_AUTO_TAG= GIT_PUT_FILE=  
  
EXPOSE 80  
CMD ["/run.sh"]

