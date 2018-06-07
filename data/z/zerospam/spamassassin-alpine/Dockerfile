FROM alpine:edge  
MAINTAINER Antoine Aflalo <dev@zerospam.ca>  
  
#Configure CamelCadeDB  
ENV PERL5_DEBUG_ROLE="client"  
ENV PERL5_DEBUG_HOST=172.17.0.1  
ENV PERL5_DEBUG_PORT=7765  
  
WORKDIR /root/  
  
RUN apk add \--no-cache build-base perl-dev perl-yaml perl-json perl-log-
log4perl perl-libwww perl-crypt-ssleay perl-digest-hmac perl-http-message
perl-mime-lite perl-net-cidr-lite perl-io-gzip bash vim wget tar perl-mail-
dkim perl-netaddr-ip perl-digest-sha1 perl-html-parser perl-net-dns gnupg
perl-yaml-syck perl-switch perl-mail-spf  
  
RUN apk add perl-json-xs --update-cache --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
  
# Make CPAN download dependencies  
RUN perl -MCPAN -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1,
autoconfig => 1); $c->edit(prerequisites_policy => "follow");
$c->edit(build_requires_install_policy => "yes"); $c->commit'  
  
#Update CPAN if needed  
RUN cpan install CPAN && cpan reload cpan  
  
RUN cpan Time::Piece Devel::Camelcadedb  
  
RUN wget http://mirror.its.dal.ca/apache//spamassassin/source/Mail-
SpamAssassin-3.4.1.tar.gz -O SpamAssassin.tar.gz\  
&& tar xfv SpamAssassin.tar.gz \  
&& rm SpamAssassin.tar.gz \  
&& mv Mail-SpamAssassin-* SpamAssassin  
  
#Remove the -T to run with Camelcadedb  
RUN mkdir ~/test-files/ \  
&& cd SpamAssassin \  
&& perl Makefile.PL \  
&& make \  
&& chmod 0700 spamassassin \  
&& sed -i -e 's/perl -T/perl -d:Camelcadedb/g' spamassassin \  
&& chmod 0555 spamassassin \  
&& mkdir -p /var/lib/spamassassin\  
/etc/mail/spamassassin/sa-update-keys/ \  
/usr/local/share/spamassassin \  
/usr/zs/etc/ \  
/root/SpamAssassin/sa-plugins \  
&& ln -s /root/SpamAssassin/sa-plugins/lib/ZS /root/SpamAssassin/lib/ZS \  
&& ln -s /root/SpamAssassin/sa-plugins/lists /usr/zs/etc/sa \  
&& make conf__install \  
&& wget http://spamassassin.apache.org/updates/GPG.KEY \  
&& ./sa-update \--import GPG.KEY \  
&& ./sa-update \  
&& rm GPG.KEY \  
&& rm -rf rules \  
&& mv sample*.txt ../test-files/ \  
&& echo "alias SA='spamassassin -D 2>&1 <'" >> /root/.bashrc  
  
ENV PATH=/root/SpamAssassin/:$PATH  
  
WORKDIR /root/test-files/  
VOLUME /etc/mail/spamassassin  
VOLUME /root/test-files/  

