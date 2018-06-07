FROM alpine:3.7  
RUN mkdir /apk  
COPY apk/botan-2.3.0-r1.apk /apk/botan-2.3.0-r1.apk  
COPY apk/log4cplus-1.2.0-r1.apk /apk/log4cplus-1.2.0-r1.apk  
COPY apk/kea-1.3.0-r0.apk /apk/kea-1.3.0-r0.apk  
COPY apk/kea-dhcp4-1.3.0-r0.apk /apk/kea-dhcp4-1.3.0-r0.apk  
COPY apk/kea-ctrl-agent-1.3.0-r0.apk /apk/kea-ctrl-agent-1.3.0-r0.apk  
COPY apk/kea-admin-1.3.0-r0.apk /apk/kea-admin-1.3.0-r0.apk  
COPY apk/kea-hook-runscript-1.1.0-r0.apk /apk/kea-hook-runscript-1.1.0-r0.apk  
COPY hook.sh /hook.sh  
  
RUN apk add --update --no-cache --allow-untrusted bash curl mariadb-client
/apk/botan-2.3.0-r1.apk /apk/log4cplus-1.2.0-r1.apk /apk/kea-1.3.0-r0.apk
/apk/kea-dhcp4-1.3.0-r0.apk /apk/kea-ctrl-agent-1.3.0-r0.apk /apk/kea-
admin-1.3.0-r0.apk /apk/kea-hook-runscript-1.1.0-r0.apk && rm -rf /apk && rm
-rf /var/cache/apk/*  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ADD kea-dhcp4.conf /etc/kea/kea-dhcp4.conf  
ADD kea-ctrl-agent.conf /etc/kea/kea-ctrl-agent.conf  
  
EXPOSE 67 67/udp  
EXPOSE 8080  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "kea-dhcp4" ]  

