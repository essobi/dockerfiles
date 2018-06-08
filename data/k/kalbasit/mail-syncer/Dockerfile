FROM alpine  
  
RUN apk add --update-cache offlineimap git make gcc g++ zlib xapian-core-dev \  
gmime-dev talloc-dev \  
&& rm -rf /var/cache/apk/*  
  
RUN cd /tmp \  
&& git clone https://github.com/notmuch/notmuch.git \  
&& cd notmuch \  
&& ./configure --prefix=/usr \  
&& make install \  
&& rm -rf /tmp/notmuch  
  
COPY start-daemon /usr/bin/start-daemon  
  
VOLUME /var/lib/mail-syncer  
VOLUME /etc/mail-syncer  
  
CMD ["offlineimap", "-c", "/etc/mail-syncer/offlineimaprc", "-u", "basic"]  

