FROM debian:stretch-slim AS haraka  
  
RUN apt-get update && \  
apt-get -y upgrade  
  
RUN apt-get -y install curl gnupg build-essential && \  
curl -sL --insecure https://deb.nodesource.com/setup_8.x | bash - && \  
apt install -y nodejs  
  
RUN npm install --unsafe-perm -g Haraka srs.js sqlite3 haraka-plugin-geoip
haraka-plugin-fcrdns haraka-plugin-asn haraka-plugin-known-senders haraka-
plugin-watch ws express  
  
FROM debian:stretch-slim  
MAINTAINER info@analogic.cz  
  
COPY \--from=haraka /usr/lib/node_modules /usr/lib/node_modules  
COPY \--from=haraka /usr/bin/nodejs /usr/bin  
COPY \--from=haraka /usr/bin/node /usr/bin  
  
RUN apt-get update && apt-get -y upgrade  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM=xterm  
ENV HTTPS="ON"  
ARG APP_ENV=prod  
ENV APP_ENV ${APP_ENV}  
  
ARG MODE=free  
ENV MODE ${MODE}  
  
ADD admin/app /opt/admin/app  
ADD admin/bin /opt/admin/bin  
ADD admin/upgrades /opt/admin/upgrades  
ADD admin/var /opt/admin/var  
ADD admin/web /opt/admin/web  
ADD admin/composer.json \  
admin/composer.lock \  
admin/phpunit.xml \  
admin/run_tests.sh \  
/opt/admin/  
  
ADD admin/src/ApiBundle /opt/admin/src/ApiBundle  
ADD admin/src/AppBundle /opt/admin/src/AppBundle  
  
ADD installation /installation  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz
/tmp/  
RUN /installation/00-preinstall.sh && \  
/installation/01-haraka.sh && \  
/installation/03-rsyslog.sh && \  
/installation/04-clamav.sh && \  
/installation/05-roundcube.sh && \  
/installation/05-free-version.sh && \  
/installation/06-admin.sh && \  
/installation/07-redis.sh && \  
/installation/08-zpush.sh && \  
tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
/installation/99-clean.sh && \  
ln -s /var/run/s6/services /services  
  
# 25 smtp  
# 110 pop3  
# 143 imap  
# 587 smtp (tls with starttls)  
# 993 imaps (tls since connect)  
# 995 pop3s (tls since connect)  
# 4190 sieve  
EXPOSE 25 80 110 143 443 587 993 995 4190  
ADD rootfs VERSION /  
  
VOLUME /data  
  
ENTRYPOINT ["/init"]  

