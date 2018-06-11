FROM alpine  
  
ENV VERSION=0.21  
RUN apk add -U curl alpine-sdk openssl openssl-dev pcre pcre-dev && \  
cd /tmp && \  
curl -L https://github.com/samr7/vanitygen/archive/$VERSION.tar.gz \  
| tar zx && \  
cd vanitygen-$VERSION && \  
make most && \  
mv keyconv vanitygen /usr/local/bin/ && \  
apk del curl alpine-sdk openssl-dev pcre-dev && \  
rm -rf /var/cache/apk/* /var/lib/apk/* /tmp/*  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

