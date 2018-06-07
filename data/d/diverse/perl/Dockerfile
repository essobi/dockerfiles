FROM alpine:3.6  
  
ENV PERL_VERSION 5.20.3  
  
RUN set -ex \  
&& CPANM_VERSION=1.7043 \  
&&
PERL_SHA256=3524e3a76b71650ab2f794fd68e45c366ec375786d2ad2dca767da424bbb9b4a \  
&&
CPANM_SHA256=68a06f7da80882a95bc02c92c7ee305846fb6ab648cf83678ea945e44ad65c65
\  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
curl \  
procps \  
&& curl -fSL https://www.cpan.org/src/5.0/perl-$PERL_VERSION.tar.gz -o
perl.tar.gz \  
&& echo "$PERL_SHA256 *perl.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/perl \  
&& tar -zxf perl.tar.gz -C /usr/src/perl --strip-components=1 \  
&& rm perl.tar.gz \  
&& cd /usr/src/perl \  
&& sed -i -e 's/less -R/less/g' ./Configure \  
&& sed -i -e 's/libswanted="\\(.*\\) nsl\\(.*\\)"/libswanted="\1\2"/g'
./Configure \  
# musl's C locale is not quite conforming (to ISO C or POSIX)  
# http://wiki.musl-libc.org/wiki/Open_Issues  
&& sed -i -e 's/ok($warned, "variable set to setlocale(BAD LOCALE) is
considered uninitialized");//g' ./lib/locale.t \  
&& ./Configure -des \  
-Dcccdlflags='-fPIC' \  
-Dcccdlflags='-fPIC' \  
-Dccdlflags='-rdynamic' \  
-Dprefix=/usr \  
-Dprivlib=/usr/share/perl5/core_perl \  
-Darchlib=/usr/lib/perl5/core_perl \  
-Dvendorprefix=/usr \  
-Dvendorlib=/usr/share/perl5/vendor_perl \  
-Dvendorarch=/usr/lib/perl5/vendor_perl \  
-Dsiteprefix=/usr/local \  
-Dsitelib=/usr/local/share/perl5/site_perl \  
-Dsitearch=/usr/local/lib/perl5/site_perl \  
-Dlocincpth=' ' \  
-Doptimize="$CFLAGS" \  
-Duselargefiles \  
-Dusethreads \  
-Duseshrplib \  
-Dd_semctl_semun \  
-Dman1dir=/usr/share/man/man1 \  
-Dman3dir=/usr/share/man/man3 \  
-Dinstallman1dir=/usr/share/man/man1 \  
-Dinstallman3dir=/usr/share/man/man3 \  
-Dman1ext='1' \  
-Dman3ext='3pm' \  
-Dcf_by='Alpine' \  
-Ud_csh \  
-Dusenm \  
&& make libperl.so \  
&& make -j$(nproc) \  
&& TEST_JOBS=$(nproc) make test_harness \  
&& make install \  
&& curl -fSL https://www.cpan.org/authors/id/M/MI/MIYAGAWA/App-
cpanminus-$CPANM_VERSION.tar.gz -o cpanm.tar.gz \  
&& echo "$CPANM_SHA256 *cpanm.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/cpanm \  
&& tar -zxf cpanm.tar.gz -C /usr/src/cpanm --strip-components=1 \  
&& rm cpanm.tar.gz \  
&& cd /usr/src/cpanm \  
&& perl bin/cpanm . \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& cd / \  
&& rm -rf /usr/src/perl \  
&& rm -rf /usr/src/cpanm \  
&& rm -rf /root/.cpanm \  
&& rm -rf /usr/share/man/* \  
&& find /usr/share/ -name "*.pod" -delete  
  
CMD ["perl","-de0"]  

