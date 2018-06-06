FROM ubuntu:14.04  
MAINTAINER Tyler Griesbach <tgriesbach@tekniq.com>  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Add the ondrej php repo  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >
/etc/apt/sources.list.d/ondrej-php-trusty.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C  
  
RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get -y -q install
php5.6 php5.6-fpm php5.6-gd php5.6-apcu \  
php5.6-sqlite php5.6-pgsql php-pear php5.6-mysql php5.6-intl php5.6-simplexml
php5.6-sybase php5.6-geoip php5.6-gmp \  
php5.6-readline php5.6-mcrypt php5.6-xmlrpc php5.6-json php5.6-curl
php5.6-soap php5.6-zip \  
rubygems-integration openssh-client wget curl exim4 libxrender1 gsfonts
libssl-dev cups  
  
# Set default php to 5.6  
RUN update-alternatives --install /usr/bin/php php /usr/bin/php5.6 100  
  
# Run the node script that adds the repo automatically  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get -y update && apt-get -y -q install nodejs  
  
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

