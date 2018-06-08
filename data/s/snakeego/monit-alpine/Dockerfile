FROM alpine:latest  
  
RUN set -x \  
&& apk \--update --no-cache add \  
curl \  
build-base \  
libressl-dev \  
file \  
zlib-dev \  
&& mkdir /srv/monit \  
&& cd /srv/monit \  
&& curl -LsS
https://bitbucket.org/tildeslash/monit/downloads/monit-5.16.tar.gz | gunzip -c
- | tar -xf - \  
&& cd monit-* \  
&& ./configure --prefix=/monit \--without-pam \  
&& make \  
&& make install \  
&& cd /monit \  
&& mkdir -p \  
etc/conf.d\  
log \  
&& echo 'set daemon 60 \  
set logfile /monit/log/monit.log \  
set pidfile /monit/monit.pid \  
set statefile /monit/monit.state \  
include /monit/etc/conf.d/*' | sed 's/^[\t ]*//g' | sed 's/[ \\\\]*$//g' >
etc/monitrc \  
&& chmod 700 etc/monitrc \  
&& ln -s /monit/bin/monit /bin \  
&& apk del \  
curl \  
build-base \  
libressl-dev \  
file \  
zlib-dev \  
&& rm -rf \  
/srv/monit \  
/var/cache/apk/*  
  
VOLUME ["/monit/etc/conf.d"]  
CMD ["monit", "-I"]

