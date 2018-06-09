FROM centos:7  
MAINTAINER Johannes Nickel <jn@znuny.com>  
MAINTAINER Ryuta Otaki <otaki.ryuta@classmethod.jp>  
  
RUN yum install -y epel-release  
RUN yum update -y  
RUN yum -y install \  
mariadb \  
procmail \  
cronie  
  
# OTRS  
RUN yum -y install
http://ftp.otrs.org/pub/otrs/RPMS/rhel/7/otrs-4.0.6-01.noarch.rpm  
  
# OTRS additional perl modules; listed by /opt/otrs/bin/otrs.CheckModules.pl
command.  
RUN yum -y install \  
"perl(Apache2::Reload)" \  
"perl(Archive::Tar)" \  
"perl(Archive::Zip)" \  
"perl(Crypt::Eksblowfish::Bcrypt)" \  
"perl(Crypt::SSLeay)" \  
"perl(Date::Format)" \  
"perl(DBI)" \  
"perl(DBD::mysql)" \  
"perl(Encode::HanExtra)" \  
"perl(GD)" \  
"perl(GD::Text)" \  
"perl(GD::Graph)" \  
"perl(IO::Socket::SSL)" \  
"perl(JSON::XS)" \  
"perl(List::Util::XS)" \  
"perl(LWP::UserAgent)" \  
"perl(Mail::IMAPClient)" \  
"perl(ModPerl::Util)" \  
"perl(Net::DNS)" \  
"perl(Net::LDAP)" \  
"perl(PDF::API2)" \  
"perl(Template)" \  
"perl(Template::Stash::XS)" \  
"perl(Text::CSV_XS)" \  
"perl(Time::HiRes)" \  
"perl(Time::Piece)" \  
"perl(XML::Parser)" \  
"perl(YAML::XS)"  
  
# OTRS additional Japanese TTF fonts for exporting various data in PDF format  
RUN yum -y install \  
ipa-gothic-fonts \  
ipa-mincho-fonts \  
ipa-pgothic-fonts \  
ipa-pmincho-fonts  
  
#OTRS COPY Configs  
ADD otrs/Config.pm /opt/otrs/Kernel/Config.pm  
RUN chgrp apache /opt/otrs/Kernel/Config.pm  
RUN chmod g+w /opt/otrs/Kernel/Config.pm  
  
#reconfigure httpd  
ADD httpd/zzz_otrs.conf /etc/httpd/conf.d/zzz_otrs.conf  
RUN rm /etc/httpd/conf.d/welcome.conf  
  
#enable crons  
WORKDIR /opt/otrs/var/cron/  
USER otrs  
CMD ["/bin/bash -c 'for foo in *.dist; do cp $foo `basename $foo .dist`;
done'"]  
  
USER root  
EXPOSE 80  
ADD run.sh /run.sh  
CMD ["/run.sh"]  

