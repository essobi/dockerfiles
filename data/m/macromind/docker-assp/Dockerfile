FROM ubuntu:16.04  
MAINTAINER Rafael Carreira <rafaelcarreira@macromind.com.br>  
  
# Install Deps  
RUN apt-get update && apt-get install -y \  
build-essential unzip wget libssl-dev libdb-dev curl software-properties-
common cpanminus \  
libxml-perl libdbd-mysql-perl pkg-config libtime-parsedate-perl git mysql-
client vim supervisor  
  
# Install Perl Deps  
RUN cpanm --force \  
Mail::SPF Mail::SPF::Query NetAddr::IP  
RUN cpanm \  
LWP::Simple Compress::Zlib Error Mail::DKIM Mail::DKIM::Verifier Digest::MD5
Digest::SHA1 Sys::CpuAffinity \  
PerlIO::scalar threads threads::shared Thread::Queue Thread::State BerkeleyDB
Crypt::CBC \  
Time::HiRes Crypt::OpenSSL::AES Email::MIME::Modifier Email::Send Email::Valid
Unicode::LineBreak Unicode::GCString \  
File::chmod File::Find::Rule File::Slurp File::Which File::ReadBackwards
File::Type MIME::Charset MIME::Types \  
LEOCHARRE::DEBUG Linux::usermod LEOCHARRE::CLI Crypt::RC4 Smart::Comments
Devel::Peek Devel::Size Devel::InnerPackage \  
Text::Glob Text::Unidecode Tie::RDBM Tie::DBI Regexp::Optimizer
Number::Compare Mail::SRS Filesys::Df \  
Convert::Scalar Convert::TNEF \  
Net::CIDR::Lite Net::DNS Net::IP::Match::Regexp Net::LDAP Net::IP
Net::SenderBase Net::Syslog Net::SMTP::SSL Net::SMTP \  
Lingua::Identify Lingua::StopWords Lingua::Stem::Snowball Archive::Zip
Archive::Tar Archive::Extract \  
IO::Compress::Base IO::Compress::Gzip IO::Socket::SSL Data::Dumper Socket6
Authen::SASL \  
IO::Compress::Bzip2 IO::Compress::RawDeflate IO::Compress::Zip
IO::Compress::Deflate IO::Wrap \  
DBD::LDAP DBD::PgPP DBD::Sprite DBD::File DBD::Log DBD::CSV DBD::Template
Sys::MemInfo \  
Crypt::SMIME Archive::Libarchive::XS HTML::Strip Schedule::Cron  
  
  
# Setup postfix  
RUN echo postfix postfix/main_mailer_type string "'Internet Site'" | debconf-
set-selections && \  
echo postfix postfix/mynetworks string "127.0.0.0/8" | debconf-set-selections
&& \  
echo postfix postfix/mailname string antispam.macromind.online | debconf-set-
selections && \  
apt-get --yes --force-yes install postfix && \  
postconf -e mydestination="antispam.macromind.online, localhost.localdomain,
localhost" && \  
postconf -e smtpd_banner='$myhostname ESMTP $mail_name' && \  
postconf -e myhostname="antispam.macromind.online" && \  
postconf -e inet_protocols=ipv4 && \  
postconf -e smtpd_client_restrictions="permit_mynetworks, reject" && \  
postconf -e smtpd_delay_reject=no && \  
postconf -e home_mailbox="Maildir/" && \  
postconf -e compatibility_level=2 && \  
postconf -e message_size_limit=81920000 && \  
postconf -e transport_maps="hash:/usr/share/assp/postfix/transport" && \  
sed -i 's/^smtp inet/125 inet/' /etc/postfix/master.cf  
  
RUN apt-get -y install rsyslog  
  
# Clean up  
RUN apt-get clean \  
&& rm -rf \  
/root/.cpan/* \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY keep-updated.sh /keep-updated.sh  
COPY remove_all_deferred.sh /remove_all_deferred.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

