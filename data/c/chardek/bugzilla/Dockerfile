FROM ubuntu:xenial  
MAINTAINER Chris Hardekopf <chrish@basis.com>  
  
# Update and install modules for bugzilla, Apache2  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -q -y supervisor gcc \  
make apache2 mysql-client expat libexpat1-dev \  
libapache2-mod-perl2 libmysqlclient-dev libmath-random-isaac-perl \  
liblist-moreutils-perl libencode-detect-perl libdatetime-perl \  
msmtp msmtp-mta libnet-ssleay-perl libcrypt-ssleay-perl \  
libappconfig-perl libdate-calc-perl libtemplate-perl libmime-perl build-
essential \  
libdatetime-timezone-perl libdatetime-perl libemail-sender-perl libemail-mime-
perl \  
libemail-mime-modifier-perl libdbi-perl libdbd-mysql-perl libcgi-pm-perl \  
libmath-random-isaac-perl libmath-random-isaac-xs-perl \  
libapache2-mod-perl2 libapache2-mod-perl2-dev libchart-perl libxml-perl \  
libxml-twig-perl perlmagick libgd-graph-perl libtemplate-plugin-gd-perl \  
libsoap-lite-perl libhtml-scrubber-perl libjson-rpc-perl libdaemon-generic-
perl \  
libtheschwartz-perl libtest-taint-perl libauthen-radius-perl libfile-slurp-
perl \  
libencode-detect-perl libmodule-build-perl libnet-ldap-perl libauthen-sasl-
perl \  
libtemplate-perl-doc libfile-mimeinfo-perl libhtml-formattext-withlinks-perl \  
libgd-dev lynx-cur graphviz python-sphinx patch && \  
rm -rf /var/lib/apt/lists/*  
  
# Remove DEFAULT apache site  
RUN rm -rf /var/www/html  
  
# Make Bugzilla install Directory  
ENV VERSION 5.0.4  
ADD https://ftp.mozilla.org/pub/mozilla.org/webtools/bugzilla-$VERSION.tar.gz
/tmp/  
RUN tar -xvf /tmp/bugzilla-$VERSION.tar.gz -C /var/www/  
RUN ln -s /var/www/bugzilla-$VERSION /var/www/html  
ADD bugzilla.conf /etc/apache2/sites-available/  
WORKDIR /var/www/html  
  
# Removing MSMTPRC file  
RUN rm -f /etc/msmtprc  
  
# Verifying all bugzilla modules are installed and running checksetup.pl  
RUN /usr/bin/perl install-module.pl Email::Send && \  
/usr/bin/perl install-module.pl File::Spec  
RUN ./install-module.pl --all  
#RUN ./checksetup.pl  
  
# Enable CGI and Disable default apache site  
RUN a2enmod cgi headers expires rewrite && a2ensite bugzilla && a2dissite
000-default  
  
# Add the start script  
ADD start /opt/  
  
# Run start script  
CMD ["/opt/start"]  
  
# Expose web server port  
EXPOSE 80  

