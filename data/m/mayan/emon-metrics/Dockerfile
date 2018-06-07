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
  
# Confiure periodic pull of google analytics data. (Work in progress
https://www.npmjs.com/package/gatographite)  
ENV GA_API_EMAIL_ADDRESS fixme #email address for monitoring account created
in ga console  
ENV GA_API_VIEW_ID fixme #ID for resources to be polled  
ENV GA_API_FRIENDLY_NAME myservice #A nice name to go with this.  
# These variables probably dont need to be changed  
ENV PATH $PATH:/usr/local/bin  
ENV GOPATH /build/go  
  
# Updates..  
# We need to add the 3.3 community repo as building a new version of  
# go from scratch is too damn difficult.  
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.3/community" >>
/etc/apk/repositories  
  
#RUN apk update && apk upgrade  
# Make the user environment more friendly (remove for production)  
RUN apk add --update curl wget bash vim  
  
# Create a couple of dirs. /build will be deleted at the end.  
RUN mkdir -p /build \  
/build/go && \  
mkdir -p /data/monit \  
/data/whisper && \  
mkdir -p /usr/local/bin  
  
# Install a load of required runtime and development packages  
RUN apk add --update py-cairo cairo-tools libffi py-yaml yaml \  
cairo-dev py-cairo-dev py-pip libffi-dev git build-base yaml-dev go wget
python-dev  
  
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
RUN apk add --update rsyslog  
ADD ./config/rsyslog/rsyslog.conf /etc/rsyslog.conf  
  
# Install and configure Monit core  
# Monit does only requires the one configuration for all uses  
RUN apk add --update monit  
RUN mkdir -p /etc/monit.d /var/monit && \  
rm -f /etc/monitrc  
ADD config/monit/monitrc /etc/monitrc  
RUN chmod 0700 /etc/monitrc  
  
# Create some users and groups  
RUN addgroup -S carbon && \  
addgroup -S relay && \  
addgroup -S graphite && \  
addgroup -S postfix  
RUN adduser -S -G carbon -D -H -h /data/whisper carbon && \  
adduser -S -G relay -D -H -h /var/tmp -s /bin/sh relay && \  
adduser -S -G graphite -D -H -h /data/carbon graphite && \  
adduser -S -G postfix -D -H -h /var/spool/postfix postfix && \  
addgroup graphite carbon  
  
# Install and configure go-carbon  
RUN cd /build && \  
git clone https://github.com/lomik/go-carbon.git && \  
cd go-carbon && \  
make submodules && \  
make && \  
install go-carbon /usr/local/bin/ && \  
mkdir -p /var/run/go-carbon /var/log/go-carbon /data/whisper && \  
chown carbon:carbon /var/run/go-carbon /var/log/go-carbon /data/whisper  
ADD config/go-carbon/* /etc/  
  
# Install and configure graphite-api  
# Next line is a reminder of how nasty cario was to get working before what I
assume were changes in alpine 3.3..  
# RUN pip install git+https://github.com/SimonSapin/cairocffi.git  
RUN pip install virtualenv && \  
/usr/bin/virtualenv /graphite-api && \  
/graphite-api/bin/pip install graphite-api gunicorn && \  
mkdir -p /data/index && \  
chown -R graphite:graphite /data/index  
ADD config/graphite-api/graphite-api.yaml /etc/  
  
# Install and configure carbon c relay  
RUN cd /build && \  
git clone https://github.com/grobian/carbon-c-relay.git && \  
cd carbon-c-relay && \  
make && \  
strip relay && \  
install relay /usr/local/bin && \  
mkdir -p /var/log/relay /var/run/relay  
ADD config/relay/*.conf /etc/  
ADD config/relay/relay_start /usr/local/bin/  
RUN chown relay:relay /var/log/relay /var/run/relay  
  
# Compile, install and configure bosun  
# Not used in this image - left here for reference  
#RUN go get bosun.org/cmd/bosun && \  
# install /build/go/bin/bosun /usr/local/bin/  
# Install and configure Nginx  
# This is used to enable basic auth on graphite-api  
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
RUN rm -rf /build && \  
rm -rf /var/cache/apk/*  
# apk del cairo-dev py-cairo-dev py-pip libffi-dev git build-base yaml-dev go
wget  
# add the entry point  
ADD startup.sh /startup.sh  
RUN chmod 700 /startup.sh  
  
VOLUME /data /config  
  
# Graphite-API listens on port 8888  
# Carbon-C-Relay listens on port 2003  
# Monit is listening on port 8889  
# Monit and Graphite-API could be proxied by Nginx  
EXPOSE 8888 2003 8889  
ENTRYPOINT /startup.sh  

