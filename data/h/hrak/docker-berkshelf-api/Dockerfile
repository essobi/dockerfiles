FROM ruby:2.3-alpine  
  
MAINTAINER Hans Rakers <h.rakers@global.leaseweb.com>  
  
COPY scripts /scripts  
  
RUN apk update && apk --update add bash build-base ruby-dev libarchive-dev
tzdata && \  
addgroup -g 262 berkshelf && \  
adduser -u 262 -G berkshelf -h /home/berkshelf -s /bin/bash -S berkshelf && \  
mkdir -p /home/berkshelf/.berkshelf/api-server && \  
mkdir -p /home/berkshelf/.chef && \  
chown berkshelf:berkshelf -R /home/berkshelf/ && \  
mv /scripts/run_berks_api.sh /usr/bin/run_berks_api.sh && \  
chmod 755 /usr/bin/run_berks_api.sh && \  
cd /scripts && bundle install && \  
ln -s /usr/local/bundle/bin/bundle /usr/bin/bundle && \  
apk del build-base ruby-dev && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 26200  
ENTRYPOINT ["/bin/bash", "-c"]  
# Run as user: berkshelf but still enable logging as root to a running  
# container with "docker exec", thus do not add: "USER berkshelf".  
CMD ["/usr/bin/run_berks_api.sh"]  

