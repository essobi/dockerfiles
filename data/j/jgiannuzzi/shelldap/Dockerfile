FROM alpine:3.4  
ENV SHELLDAP_VERSION 1.3.2  
ENV SHELLDAP_SHA512
b4f84cfa164e69c7bdcbbd39416900190df8acf701539fbf0f2576514961c683  
  
RUN set -ex \  
&& apk add --no-cache perl perl-yaml-syck perl-net-ldap perl-io-socket-ssl
perl-authen-sasl perl-digest-md5 perl-term-readkey \  
&& apk add --no-cache --virtual .build-deps perl-dev make ncurses-dev gcc
musl-dev readline-dev \  
&& echo y | cpan \  
&& cpan Term::Shell Algorithm::Diff Term::ReadLine::Gnu \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .shelldap-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf ~/.cpan  
  
RUN set -ex \  
&& apk add --no-cache openssl \  
&& wget
https://bitbucket.org/mahlon/shelldap/downloads/shelldap-${SHELLDAP_VERSION}.tar.gz
\  
&& apk del openssl \  
&& echo "${SHELLDAP_SHA512} shelldap-${SHELLDAP_VERSION}.tar.gz" | sha256sum
-c - \  
&& tar xzvf shelldap-${SHELLDAP_VERSION}.tar.gz \  
&& mv shelldap-${SHELLDAP_VERSION}/shelldap /usr/local/bin \  
&& rm -rf shelldap-${SHELLDAP_VERSION} shelldap-${SHELLDAP_VERSION}.tar.gz  
  
RUN set -ex \  
&& apk add --no-cache vim \  
&& echo "set background=dark" >> /etc/vim/vimrc  
  
ENV EDITOR vim  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["shelldap"]  

