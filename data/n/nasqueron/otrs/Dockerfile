#  
# Docker image for OTRS installation  
# Based on initial work by Johannes Nickel <jn@znuny.com>  
#  
FROM centos:centos6  
MAINTAINER Sébastien Santoro aka Dereckson <dereckson+nasqueron-docker@espace-
win.org>  
  
#  
# Environment (overridable)  
#  
ENV OTRS_VERSION 4.0.8-02  
ENV DB_NAME otrs  
  
#  
# Required software  
#  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum update -y && \  
yum -y install wget mysql curl procmail \  
apache httpd httpd-devel \  
perl-core mod_perl \  
"perl(Crypt::SSLeay)" "perl(Date::Format)" \  
"perl(Net::LDAP)" "perl(URI)" "perl(GD)" \  
"perl(LWP::UserAgent)" "perl(Net::DNS)" \  
"perl(IO::Socket::SSL)" "perl(XML::Parser)" \  
"perl(YAML::XS)" "perl(Apache2::Reload)" \  
"perl(Crypt::Eksblowfish::Bcrypt)" "perl(DBD::mysql)" \  
"perl(GD::Text)" "perl(GD::Graph)" "perl(JSON::XS)" \  
"perl(Mail::IMAPClient)" "perl(Encode::HanExtra)" \  
"perl(PDF::API2)" "perl(Text::CSV_XS)" "perl(YAML::XS)" && \  
wget http://ftp.otrs.org/pub/otrs/RPMS/rhel/6/otrs-${OTRS_VERSION}.noarch.rpm
&& \  
yum -y install otrs-${OTRS_VERSION}.noarch.rpm --skip-broken  
  
#  
# Configuration files  
#  
COPY files /  
RUN sed -i -e"s/mod_perl.c/mod_perl.so/" /etc/httpd/conf.d/zzz_otrs.conf && \  
sed -i "s/error\/noindex.html/otrs\/index.pl/" /etc/httpd/conf.d/welcome.conf  
  
EXPOSE 80  
CMD ["/bin/bash", "/run.sh"]  

