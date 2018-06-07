FROM tmacro/base  
  
ENV GOPATH /go  
ENV LEGO_PROVIDER cloudflare  
ENV LEGO_DNS_RESOLVERS 8.8.8.8  
ENV LEGO_PATH /lego  
ENV LEGO_HOOKS_DIR $LEGO_PATH/hooks  
ENV LEGO_KEY_TYPE ec384  
ENV LEGO_RENEW_DAYS 30  
RUN apk_add ca-certificates && \  
apk_add --virtual build-deps zlib-dev \  
openssl-dev \  
build-base \  
linux-headers \  
go \  
git && \  
go get -u github.com/xenolf/lego && \  
cd /go/src/github.com/xenolf/lego && \  
go build -o /usr/bin/lego . && \  
apk del build-deps && \  
rm -rf /var/cache/apk/* && \  
rm -rf /go  
  
COPY ./issue-certs ./lego-config /usr/bin/  
RUN chmod +x /usr/bin/issue-certs  
  
COPY ./s6 /etc  
COPY crontab /var/spool/cron/crontabs/root  
ENTRYPOINT /init  
  

