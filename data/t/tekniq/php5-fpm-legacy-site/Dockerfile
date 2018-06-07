FROM ubuntu:14.04  
MAINTAINER Tyler Griesbach <tgriesbach@tekniq.com>  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get -y -q install
php5-cli php5-fpm php5-gd php5-apcu \  
php5-sqlite php5-pgsql php-pear php5-mysql php5-intl php5-sybase php5-geoip
php5-gmp \  
php5-readline php5-mcrypt php5-apcu php5-xmlrpc php5-json php5-curl \  
rubygems-integration openssh-client wget curl exim4 libxrender1 gsfonts
libssl-dev  
  
RUN wget http://tek-lin-devop.tekniq.com/wkhtmltopdf-0.11.0_rc1-static-
amd64.tar.bz2  
RUN tar xvjf wkhtmltopdf-0.11.0_rc1-static-amd64.tar.bz2  
RUN install wkhtmltopdf-amd64 /usr/bin/wkhtmltopdf  
RUN install wkhtmltopdf-amd64 /usr/local/bin/wkhtmltopdf  
  
RUN gem install sass  
  
# Configure Exim4, our SMTP server  
RUN rm -rf /etc/exim4 && mkdir -p /etc/exim4  
ADD exim4.conf /etc/exim4/exim4.conf  
  
VOLUME ["/hosting_files"]  
  
EXPOSE 9000  
EXPOSE 25  
ADD run.sh /start  
RUN chmod +x /start  
  
ENTRYPOINT ["/start"]

