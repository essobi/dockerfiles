FROM alpine:3.3  
MAINTAINER Michael Gerdemann <michael@gerdemann.me>  
  
# Add commonly used packages  
RUN apk add --update bind-tools && \  
rm -rf /var/cache/apk/*  
  
# Add the files  
ADD root /  
  
#ENTRYPOINT ["/init"]  
#CMD []  
  
RUN apk add --update nginx=1.8.1-r0 && \  
rm -rf /var/cache/apk/* && \  
chown -R nginx:www-data /var/lib/nginx && \  
mkdir -p /data /var/lib/nginx/tmp/ && \  
chown -R nginx:www-data /data /var/lib/nginx/tmp/  
# Expose the ports for nginx  
EXPOSE 80 443  
  
WORKDIR /data  
VOLUME ["/data"]

