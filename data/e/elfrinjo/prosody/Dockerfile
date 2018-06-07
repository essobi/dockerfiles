FROM alpine:latest  
  
MAINTAINER J. Elfring <devops@elfrinjo.de>  
  
## Install Packages  
RUN apk add --no-cache --update \  
libcrypto1.0 libidn lua lua-expat lua-filesystem lua-sec lua-socket  
  
## Prosody shall see SSL certs from letsencrypt  
## (linked from a different container)  
RUN addgroup -S -g 114 ssl-cert \  
&& adduser daemon ssl-cert  
  
## Install build envirnoment, build and remove unneeded things  
## This is done in one step to reduce image size  
RUN apk add --update --no-cache --virtual .build-deps \  
alpine-sdk git mercurial luarocks linux-headers lua-dev libidn-dev openssl-dev
\  
&& luarocks-5.1 install luabitop \  
&& hg clone https://hg.prosody.im/trunk /prosody-trunk \  
&& cd /prosody-trunk \  
&& ./configure --no-example-certs --cflags='-fPIC -Wall -std=c89 -pedantic
-D_GNU_SOURCE' \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /prosody-trunk \  
&& hg clone https://hg.prosody.im/prosody-modules/ /usr/local/lib/prosody-
community-modules \  
&& rm -rf /usr/local/lib/prosody-community-modules/.hg \  
&& rm -rf /usr/local/lib/prosody-community-modules/.hgtags \  
&& apk del .build-deps  
  
COPY ./assets/prosody.cfg.lua /usr/local/etc/prosody/prosody.cfg.lua  
RUN chown daemon:daemon /usr/local/var/lib/prosody  
  
EXPOSE 5222 5269 5347 5280 5281  
VOLUME ["/usr/local/etc/prosody", "/usr/local/var/lib/prosody"]  
  
USER daemon  
ENTRYPOINT ["/usr/local/bin/prosody"]  
  

