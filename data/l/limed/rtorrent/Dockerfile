FROM limed/alpine-base  
MAINTAINER limed@sudoers.org  
  
RUN apk --no-cache add rtorrent screen\  
&& addgroup -g 1000 rtorrent \  
&& addgroup -g 111 user \  
&& adduser -D -u 1000 -G user -G rtorrent rtorrent \  
&& mkdir -p /data/rtorrent \  
&& mkdir -p /config/logs \  
&& touch /config/logs/rtorrent.log \  
&& rm -rf /var/cache/apk/*  
  
COPY files/startup.sh /app  
COPY files/rtorrent.rc /config  
  
VOLUME /data/rtorrent  
VOLUME /config  
VOLUME /app  
  
EXPOSE 49300  
EXPOSE 5000  
CMD [ '/app/startup.sh' ]  

