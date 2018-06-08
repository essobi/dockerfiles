FROM johanadriaans/docker-base-alpine:3.4  
MAINTAINER Johan Adriaans <johan@shoppagina.nl>  
  
RUN apk add \--update ssmtp curl mailx drbd-utils perl e2fsprogs  
  
COPY files/drbd.d /etc/drbd.d  
COPY service /etc/service  
COPY files/ssmtp.conf /etc/ssmtp/ssmtp.conf  
COPY files/aliases /etc/aliases  
COPY files/monitor-connectivity.sh /usr/bin/monitor-connectivity.sh  
  
ENV DRBD_DEVICE=/dev/sdxxx  
ENV EMAIL_ROOT_ACCOUNT=info@dummy-domain.xyz  
ENV SMTP_SERVER=server.xyz:587  
ENV SMTP_USER=smtp-user  
ENV SMTP_PASS=smtpPassw0rd  
ENV SMTP_REWRITE_DOMAIN=outgoung-mail-domain.xyz  
ENV DRBD_HOSTNAME_1=cluster-data-1  
ENV DRBD_HOSTNAME_2=cluster-data-2  
ENV DRBD_ADDRESS_1=10.0.0.3:7789  
ENV DRBD_ADDRESS_2=10.0.0.4:7789  
ENV DRBD_SECRET=drbdSharedSecret  
  
ENTRYPOINT ["/sbin/dumb-init", "/sbin/runsvdir", "-P", "/etc/service"]  

