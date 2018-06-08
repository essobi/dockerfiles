# Chris Weyl <cweyl@alumni.drew.edu> 2017  
  
FROM alpine:3.6  
MAINTAINER Chris Weyl <cweyl@alumni.drew.edu>  
  
ENV TZ=UTC  
  
RUN apk update && \  
apk add \  
wget make gcc perl perl-dev musl-dev \  
perl-apache-logformat-compiler \  
perl-archive-zip \  
perl-b-hooks-endofscope \  
perl-carp \  
perl-carp-clan \  
perl-cgi \  
perl-cgi-emulate-psgi \  
perl-cgi-psgi \  
perl-class-accessor \  
perl-class-accessor-chained \  
perl-class-method-modifiers \  
perl-class-methodmaker \  
perl-clone \  
perl-config-any \  
perl-config-inifiles \  
perl-config-simple \  
perl-config-tiny \  
perl-cpan-meta-check \  
perl-cpanel-json-xs \  
perl-data-compare \  
perl-data-dump \  
perl-data-dumper \  
perl-data-guid \  
perl-data-optlist \  
perl-data-page \  
perl-data-page-pageset \  
perl-data-uuid \  
perl-datetime \  
perl-datetime-format-builder \  
perl-datetime-format-natural \  
perl-datetime-format-strptime \  
perl-datetime-locale \  
perl-datetime-timezone \  
perl-dbd-sqlite \  
perl-dbi \  
perl-dbix-contextualfetch \  
perl-dbix-dbschema \  
perl-dbix-searchbuilder \  
perl-digest-bubblebabble \  
perl-digest-hmac \  
perl-digest-md5 \  
perl-digest-perl-md5 \  
perl-digest-sha1 \  
perl-dist-checkconflicts \  
perl-encode \  
perl-extutils-cchecker \  
perl-extutils-config \  
perl-extutils-depends \  
perl-extutils-helpers \  
perl-extutils-installpaths \  
perl-extutils-libbuilder \  
perl-extutils-pkgconfig \  
perl-file-copy-recursive \  
perl-file-find-rule \  
perl-file-remove \  
perl-file-sharedir \  
perl-file-sharedir-install \  
perl-file-slurp \  
perl-file-slurp-tiny \  
perl-file-temp \  
perl-file-which \  
perl-hash-merge-simple \  
perl-http-body \  
perl-http-cookies \  
perl-http-daemon \  
perl-http-message \  
perl-http-server-simple \  
perl-http-server-simple-psgi \  
perl-json \  
perl-json-maybexs \  
perl-list-allutils \  
perl-list-moreutils \  
perl-log-any \  
perl-log-dispatch \  
perl-log-dispatch-config \  
perl-log-dispatch-configurator-any \  
perl-log-log4perl \  
perl-lwp-mediatypes \  
perl-lwp-protocol-https \  
perl-lwp-useragent-determined \  
perl-mime-types \  
perl-module-build \  
perl-module-build-tiny \  
perl-module-implementation \  
perl-module-install \  
perl-module-runtime \  
perl-module-scandeps \  
perl-module-versions-report \  
perl-mojolicious \  
perl-moo \  
perl-moose \  
perl-moox-types-mooselike \  
perl-mro-compat \  
perl-namespace-autoclean \  
perl-namespace-clean \  
perl-net-server \  
perl-params-validate \  
perl-params-validationcompiler \  
perl-path-class \  
perl-path-tiny \  
perl-plack \  
perl-pod-coverage \  
perl-posix-strftime-compiler \  
perl-role-tiny \  
perl-scalar-list-utils \  
perl-scope-guard \  
perl-scope-upper \  
perl-specio \  
perl-sql-translator \  
perl-stream-buffered \  
perl-string-shellquote \  
perl-sub-exporter \  
perl-sub-exporter-progressive \  
perl-sub-identify \  
perl-sub-info \  
perl-sub-install \  
perl-sub-name \  
perl-sub-uplevel \  
perl-template-toolkit \  
perl-term-progressbar \  
perl-term-readkey \  
perl-term-table \  
perl-test-deep \  
perl-test-differences \  
perl-test-exception \  
perl-test-failwarnings \  
perl-test-fatal \  
perl-test-most \  
perl-test-taint \  
perl-test-tcp \  
perl-text-csv \  
perl-text-csv_xs \  
perl-text-template \  
perl-timedate \  
perl-tree-simple \  
perl-try-tiny \  
perl-type-tiny \  
perl-uri \  
perl-yaml \  
perl-yaml-syck \  
perl-yaml-tiny \  
perl-yaml-xs \  
&& \  
rm -r /var/cache/  
  
COPY cpanm /bin/cpanm  
  
RUN cpanm -q \  
Devel::OverloadInfo \  
App::cpanoutdated \  
UNIVERSAL::can \  
MooseX::AttributeShortcuts \  
Smart::Comments \  
Dist::Zilla \  
Catalyst::Devel \  
SQL::Translator \  
Test::Moose::More \  
Reindeer \  
|| ( cat "$HOME/.cpanm/build.log" ; exit 1 ) \  
&& rm -rf "$HOME/.cpanm/"  
  
ENTRYPOINT [ "perl" ]  

