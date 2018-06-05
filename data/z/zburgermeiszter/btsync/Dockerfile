FROM zburgermeiszter/usermode:alpine-3.3_glibc-2.23  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
LABEL com.getsync.version="2.3.7"  
  
USER root  
  
RUN apk --update --no-cache add tar curl && \  
curl -s -k -L "https://download-cdn.getsync.com/2.3.7/linux-x64/BitTorrent-
Sync_x64.tar.gz" | tar -xzf - -C /usr/sbin btsync && \  
apk del tar curl && \  
rm -rf /var/cache/apk/*  
  
COPY btsync.conf /etc/  
COPY run_sync /opt/  
  
ENV USERID 1000  
ENV GROUPID 1000  
VOLUME /mnt/sync  
  
RUN chown -R 1000:1000 \  
/etc/btsync.conf \  
/mnt/sync \  
/opt/run_sync \  
/usr/sbin/btsync  
  
USER user  
EXPOSE 8888 55555 55555/udp  
  
ENTRYPOINT ["/opt/run_sync"]  
CMD ["--log", "--config", "/etc/btsync.conf"]

