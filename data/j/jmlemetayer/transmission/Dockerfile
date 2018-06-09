FROM alpine:3.5  
# Install su-exec for easy step-down from root  
RUN set -x \  
&& apk --no-cache add su-exec  
  
# Install transmission  
RUN set -x \  
&& apk --no-cache add transmission-daemon \  
&& mkdir -p /var/lib/transmission/config \  
&& mkdir -p /var/lib/transmission/downloads \  
&& mkdir -p /var/lib/transmission/incomplete \  
&& mkdir -p /var/lib/transmission/watch  
  
VOLUME ["/var/lib/transmission/config", \  
"/var/lib/transmission/downloads", \  
"/var/lib/transmission/incomplete", \  
"/var/lib/transmission/watch"]  
WORKDIR /var/lib/transmission  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 9091  
EXPOSE 51413  
  
CMD ["transmission-daemon", "--foreground", \  
"--config-dir=/var/lib/transmission/config", \  
"--download-dir=/var/lib/transmission/downloads", \  
"--incomplete-dir=/var/lib/transmission/incomplete", \  
"--watch-dir=/var/lib/transmission/watch"]  

