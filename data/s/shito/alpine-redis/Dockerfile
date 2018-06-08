FROM alpine:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
RUN echo "ipv6" >> /etc/modules  
  
# Add Redis  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
redis  
  
# Remove cache  
RUN rm -fr /var/cache/apk/*  
  
# Expose Ports  
EXPOSE 6379  
ENTRYPOINT ["/usr/bin/redis-server"]

