FROM alpine:latest  
WORKDIR /home/ircd  
VOLUME /home/ircd/run/logs  
ENTRYPOINT ["/home/ircd/run/bin/ircd", "-foreground"]  
  
RUN ELEMENTAL_VERSION="6.6.5" \  
&& BUILD_PKGS="curl tar gcc make musl-dev bison flex openssl-dev file" \  
&& apk upgrade --no-cache && apk add --no-cache openssl $BUILD_PKGS \  
&& addgroup -S -g 1000 ircd && adduser -SDh /home/ircd -G ircd -s
/sbin/nologin -u 1000 ircd \  
&& mkdir /home/ircd/src && cd /home/ircd/src \  
&& curl -L https://github.com/Elemental-IRCd/elemental-ircd/archive/elemental-
ircd-$ELEMENTAL_VERSION.tar.gz | tar xz --strip-components=1 \  
&& ./configure --prefix=/home/ircd/run && make install \  
&& apk del --rdepends $BUILD_PKGS \  
&& rm -r /home/ircd/src /home/ircd/run/etc/* \  
&& chown -R ircd /home/ircd/run  
  
USER ircd  

