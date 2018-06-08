FROM avastsoftware/alpine-perl  
MAINTAINER Kevin Eye <kevineye@gmail.com>  
  
RUN apk add -U curl make perl-io-socket-ssl perl-digest-sha1 gpgme \  
&& cd /usr/local/bin \  
&& curl -LsSO
https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm \  
&& chmod +x cpanm \  
&& cpanm --no-wget --notest Module::Signature \  
&& cpanm --verify --no-wget --notest JSON::Any \  
&& mkdir /usr/local/src \  
&& cd /usr/local/src \  
&& curl -LsSO http://superb-
sea2.dl.sourceforge.net/project/ddclient/ddclient/ddclient-3.8.3.tar.bz2 \  
&& echo '8668d8828a74ef4e7bca90890d7bbe414c37c3ff *ddclient-3.8.3.tar.bz2' |
sha1sum -c - \  
&& tar xjf ddclient-3.8.3.tar.bz2 \  
&& ln -s /usr/local/src/ddclient-3.8.3/ddclient /usr/local/bin \  
&& apk del curl make gpgme \  
&& mkdir /var/cache/ddclient \  
&& rm -rf /root/.cpanm /usr/local/bin/cpanm /tmp/* /var/cache/apk/*  
  
ENTRYPOINT []  
CMD ["ddclient", "-foreground", "-daemon", "1800"]  

