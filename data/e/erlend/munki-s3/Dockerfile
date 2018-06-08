FROM alpine:3.6  
  
ENV S3_REGION="eu-west-1" SSL_PATH="/var/lib/puppet/ssl" SSL_NAME="munki"  
  
RUN apk add -U dumb-init nginx-mod-http-lua nginx-mod-http-set-misc && \  
sed -e "1 adaemon off;" \  
-e "s|\\(error_log\\) [^ ]*|\1 /dev/stderr|" \  
-e "s|\\(access_log\\) [^ ]*|\1 /dev/stdout|" \  
-e "s|#\\(resolver\\) [^;]*|\1 172.16.0.23 valid=300s|" \  
-i /etc/nginx/nginx.conf && \  
mkdir -p /run/nginx && \  
rm /var/cache/apk/*  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

