FROM alpine:3.6  
MAINTAINER Pierre van Sabben <pvs@ivaldi.dk>  
  
RUN apk update \  
&& apk add apcupsd openssh-client sshpass msmtp mailx \  
&& rm -rf /var/cache/apk/*  
  
COPY msmtp-wrapper /usr/bin/msmtp-wrapper  
RUN chmod +x /usr/bin/msmtp-wrapper  
  
COPY mail.rc /etc/mail.rc  
  
COPY apcupsd.conf /etc/apcupsd/apcupsd.conf  
  
COPY config /etc/apcupsd/config  
  
COPY doshutdown /etc/apcupsd/doshutdown  
RUN chmod +x /etc/apcupsd/doshutdown  
  
CMD apcupsd -b  

