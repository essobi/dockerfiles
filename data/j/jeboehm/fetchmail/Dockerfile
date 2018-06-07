FROM alpine:3.4  
MAINTAINER Jeffrey Boehm "jeff@ressourcenkonflikt.de"  
RUN apk --no-cache add fetchmail ca-certificates  
  
VOLUME /var/lib/fetchmail  
RUN chown fetchmail /var/lib/fetchmail  
  
ONBUILD COPY fetchmailrc /etc/fetchmailrc  
ONBUILD RUN chown fetchmail /etc/fetchmailrc && \  
chmod 400 /etc/fetchmailrc  
  
ONBUILD USER fetchmail  
ONBUILD CMD ["fetchmail", "-d", "900", "-N", "-f", "/etc/fetchmailrc", "-vv"]  

