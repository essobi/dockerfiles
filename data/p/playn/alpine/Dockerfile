FROM alpine:latest  
  
RUN apk \--update add \--no-cach tzdata && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk del \--purge tzdata && \  
rm -rf /var/cache/apk/*

