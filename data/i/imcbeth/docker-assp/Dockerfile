#Creating Images for ASSP web service  
FROM gliderlabs/alpine:edge  
MAINTAINER Ian McBeth <imcbeth@network-ops.ca>  
  
ENV TZ=America/Edmonton  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apk update  
## RUN apk --upgrade busybox  
RUN true && \  
apk add \--update tzdata postfix bash supervisor perl perl-sys-hostname-long
perl-net-dns make automake gcc \  
perl-lwp-protocol-https perl-dbd-pg perl-dbd-mysql perl-dbd-sqlite perl-cgi-
psgi perl-cgi perl-fcgi perl-term-readkey \  
perl-xml-rss perl-crypt-ssleay perl-crypt-eksblowfish perl-crypt-x509 perl-
html-mason-psgihandler perl-fcgi-procmanager \  
perl-mime-types perl-list-moreutils perl-json perl-html-quoted perl-html-
scrubber perl-email-address perl-text-password-pronounceable \  
perl-email-address-list perl-html-formattext-withlinks-andtables perl-html-
rewriteattributes perl-text-wikiformat perl-text-quoted \  
perl-datetime-format-natural perl-date-extract perl-data-guid perl-data-ical
perl-string-shellquote perl-convert-color perl-dbix-searchbuilder \  
perl-file-which perl-css-squish perl-tree-simple perl-plack perl-log-dispatch
perl-module-versions-report perl-symbol-global-name \  
perl-devel-globaldestruction perl-parallel-prefork perl-cgi-emulate-psgi perl-
text-template perl-net-cidr perl-apache-session \  
perl-locale-maketext-lexicon perl-locale-maketext-fuzzy perl-regexp-common-
net-cidr perl-module-refresh perl-date-manip perl-regexp-ipv6 \  
perl-text-wrapper perl-universal-require perl-role-basic perl-convert-binhex
perl-test-sharedfork perl-test-tcp perl-server-starter \  
perl-starlet perl-dev libc-dev && \  
(rm "/tmp/"* 2>/dev/null || true) && (rm -rf /var/cache/apk/* 2>/dev/null ||
true)  
  
COPY ./assp /usr/share/assp  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY postfix.sh /postfix.sh  
COPY assp.sh /assp.sh  
RUN chmod +x /postfix.sh  
RUN chmod +x /assp.sh  
  
#Exposing tcp ports  
EXPOSE 55555  
EXPOSE 125  
EXPOSE 25  
  
#Adding volumes  
VOLUME ["/var/spool/postfix", "/etc/postfix", "/usr/share/assp"]  
  
# Running final script  
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

