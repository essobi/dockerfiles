FROM avastsoftware/alpine-perl  
MAINTAINER Kevin Eye <kevineye@gmail.com>  
  
RUN apk -U add curl build-base perl-sub-name \  
&& curl -sL https://cpanmin.us | perl - --no-wget --notest AnyEvent::MQTT
AnyEvent::Run \  
&& mkdir /build \  
&& cd /build \  
&& curl -LsSO http://www.heyu.org/download/heyu-2.11-rc1.tar.gz \  
&& echo 'f02fa53b866343f05d57a2ac87c7f7b39c786295 *heyu-2.11-rc1.tar.gz' |
sha1sum -c - \  
&& tar xzf heyu-2.11-rc1.tar.gz \  
&& cd heyu-2.11-rc1 \  
&& ./configure --sysconfdir=/etc \  
&& make \  
&& make install \  
&& cd / \  
&& apk --purge del curl build-base \  
&& rm -rf /build /root/.cpanm /etc/ssl /var/cache/apk/* /lib/apk/db/*  
  
RUN cp -r /etc/heyu /etc/heyu.default \  
&& mkdir -p /usr/local/var/tmp/heyu \  
&& mkdir -p /usr/local/var/lock \  
&& chmod 777 /usr/local/var/tmp/heyu \  
&& chmod 777 /usr/local/var/lock  
  
VOLUME /etc/heyu  
  
COPY heyu-run.sh /usr/local/bin/heyu-run  
COPY heyu-mqtt.pl /usr/local/bin/heyu-mqtt  
  
ENV PERL_ANYEVENT_VERBOSE=7  
ENTRYPOINT []  
CMD heyu-run  

