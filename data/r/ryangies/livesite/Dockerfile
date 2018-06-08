FROM centos:centos7  
MAINTAINER Ryan Gies <ryangies@cpan.org>  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release deltarpm; yum clean all  
RUN yum -y install \  
openssh-clients \  
which \  
gcc \  
make \  
wget \  
tar \  
rsync \  
vim \  
perl \  
perl-devel \  
perl-CPAN \  
perl-App-cpanminus \  
httpd \  
httpd-devel \  
pcre-devel \  
mod_perl \  
mod_perl-devel \  
libapreq2 \  
perl-libapreq2 \  
subversion \  
mariadb-server \  
mariadb \  
mariadb-devel \  
gd \  
gd-devel  
  
RUN cpanm \  
CGI::Cookie \  
Moose \  
GD \  
GD::Image \  
Error \  
Error::Simple \  
Try::Tiny \  
Term::Size \  
Time::CTime \  
Math::Symbolic \  
JSON::XS \  
YAML::XS \  
Image::Size \  
Image::ExifTool \  
Time::Piece \  
DateTime \  
DateTime::TimeZone \  
Crypt::RSA \  
Data::UUID \  
Net::FTP::File \  
Mail::Sender \  
File::Type \  
Email::Valid \  
Email::Simple::Creator \  
Email::MIME::Creator \  
Email::Sender \  
Email::Sender::Simple \  
Email::Sender::Transport::SMTP \  
Email::Sender::Transport::SMTP::TLS \  
Authen::SASL \  
JavaScript::Minifier::XS \  
CSS::Minifier::XS \  
URL::Encode  
  
# Create runtime directories  
RUN mkdir \  
/var/www/config \  
/var/www/lib \  
/var/www/logs \  
/var/www/tmp  
RUN chmod 777 /var/www/tmp  
  
# Add the web server startup and configuration  
COPY run-httpd.sh /run-httpd.sh  
RUN chmod 755 /run-httpd.sh  
COPY www-livesite.conf /etc/httpd/conf.d/www.conf  
  
# Install the latest livesite distribution to the system  
COPY livesite-latest.run /tmp/livesite-latest.run  
RUN cd /tmp \  
&& ./livesite-latest.run install -y  
  
# Stub things out for vanilla run  
COPY default/livesite.hf /var/www/config  
COPY default/users /var/www/config  
COPY default/index.html /var/www/html  
  
# Default run configuration  
EXPOSE 80  
CMD ["/run-httpd.sh"]  

