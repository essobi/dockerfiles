FROM alpine:3.3  
MAINTAINER Matthew Hollick <matthew@mayan-it.co.uk>  
  
# Variables controlling sending of email via Amazon SNS  
ENV EMAIL_USER mjh  
ENV EMAIL_PASS rocks  
ENV EMAIL_SERVER email-smtp.eu-west-1.amazonaws.com:25  
ENV EMAIL_ALERT_ADDR matthew@mayan-it.co.uk  
  
# variables controlling flow and storage of carbon data  
ENV CENTRAL_METRICS_SERVER none  
ENV CARBON_LOCAL_RETENTION 10s:72h  
ENV CARBON_CENTRAL_RETENTION 60s:600d  
ENV HOSTING local  
ENV LOCATION london  
ENV SERVICE testservice  
ENV ENVIRONMENT test  
  
# Configure syslog  
ENV SYSLOG_HOST none  
  
# These variables probably dont need to be changed  
ENV PATH $PATH:/usr/local/bin  
ENV GOPATH /build/go  
  
# Updates..  
# We need to add the 3.3 community repo as building a new version of  
# go from scratch is too damn difficult.  
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.3/community" >>
/etc/apk/repositories  
  
#RUN apk update && apk upgrade  
RUN apk add --update curl wget bash vim  
  
# Create a couple of dirs. /build will be deleted at the end.  
RUN mkdir -p /build \  
/build/go && \  
mkdir -p /data/monit \  
/data/bosun && \  
mkdir -p /usr/local/bin && \  
mkdir -p /cache/apk && \  
ln -s /var/lib/apk /cache/apk  
  
# Install a load of required runtime and development packages  
RUN apk add --update git build-base go wget  
  
## Some level of hackyness to install glibc so that we can use binarys as
distributed by Bosun and Grafana and not compile them  
# Leaving this here as it might be useful some day....  
#RUN cd /build \  
# && wget -c https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk \  
# && apk add --allow-untrusted glibc-2.21-r2.apk  
# Install and configure rsyslog  
# We need rsyslog as we cant feed up log files through Monit (maybe a feature
request for monit?)  
# This could do with being replaced somehow as it is not very Docker-ific  
RUN apk add --update rsyslog  
ADD ./config/rsyslog/rsyslog.conf /etc/rsyslog.conf  
  
# Install and configure Monit core  
# Monit does only requires the one configuration for all uses  
# Maybe monit is not really needed for this docker image - but hey, its our
standard  
RUN apk add --update monit  
RUN mkdir -p /etc/monit.d /var/monit && \  
rm -f /etc/monitrc  
ADD config/monit/monitrc /etc/monitrc  
RUN chmod 0700 /etc/monitrc  
  
# Create some users and groups  
RUN addgroup -S bosun && \  
addgroup -S postfix  
RUN adduser -S -G bosun -D -H -h /data/bosun bosun && \  
adduser -S -G postfix -D -H -h /var/spool/postfix postfix  
  
# Compile, install and configure bosun  
# Not used in this image - left here for reference  
RUN go get bosun.org/cmd/bosun && \  
install /build/go/bin/bosun /usr/local/bin/  
  
ADD config/bosun/bosun.conf /etc/bosun.conf  
  
# Install and configure Nginx  
# This to be used to enable basic auth on bosun  
# RUN apk add --update nginx  
# ADD config/nginx/nginx.conf /etc/nginx.conf  
# Install and configure postfix  
RUN apk add --update postfix && \  
mv /etc/postfix/main.cf /etc/postfix/main.cf.DIST  
ADD config/postfix/* /etc/postfix/  
  
# Leaving this here so that I can refer to it when writing the startup script  
# echo "email-smtp.eu-west-1.amazonaws.com:25 ${EMAIL_USER}:${EMAIL_PASS}" >>
/etc/postfix/sasl_password  
# echo "/.+@.+/ ${ALERT_EMAIL_ADDR}" > /etc/postfix/virtual-regexp  
# postmap hash:/etc/postfix/sasl_passwd && \  
# chown root:root /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db && \  
# chmod 0600 /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db  
# postmap /etc/postfix/virtual-regexp  
# postmap /etc/postfix/virtual  
# Cleanup  
RUN rm -rf  
# rm -rf /var/cache/apk/*  
# apk del cairo-dev py-cairo-dev py-pip libffi-dev git build-base yaml-dev go
wget  
# add the entry point  
ADD startup.sh /startup.sh  
RUN chmod 700 /startup.sh  
  
VOLUME /data /config /cache  
  
EXPOSE 3000 8889  
ENTRYPOINT /startup.sh  

