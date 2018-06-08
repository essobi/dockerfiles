# This is an alpine linux based tiny qmail server image  
# It includes only smtp and send daemon that managed by supervisor.  
FROM alpine:3.4  
  
MAINTAINER Cagri Ersen <cagri.ersen@secopstech.io>  
  
ADD ./scripts /scripts  
  
RUN apk --no-cache add libstdc++ gcc make g++ openssl openssl-dev curl groff
&& \  
chmod +x /scripts/* && \  
sh /scripts/qmail-installer && \  
rm -rf /usr/src/* && \  
rm -f /package/*.tar.gz && \  
apk --no-cache del gcc make g++ openssl openssl-dev curl groff && \  
rm -rf /var/cache/apk/*  
  
# This will use daemontools to start qmail  
CMD qmail-configurator init-fqdn ${QMAIL_HOSTNAME}; \  
qmail-configurator init-relay ${RELAYIP}; \  
exec /command/svscanboot

