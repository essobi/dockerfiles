FROM ubuntu:14.04  
MAINTAINER Mohamed Abdulmoghni <mabdulmoghni@cloud9ers.com>  
############################################################################################  
RUN echo 'export PATH=/usr/local/rvm/bin:$PATH\n \  
export PATH=/usr/local/rvm/rubies/ruby-2.0.0-p648/bin:$PATH\n \  
export GEM_HOME=/usr/local/rvm/rubies/ruby-2.0.0-p648\n \  
export GEM_PATH=/usr/local/rvm/rubies/ruby-2.0.0-p648' >> /root/.bashrc  
############## update Image
#################################################################  
### Ensure up to date system  
### apache and its ruby webserver prerequisites setup  
### Clean up APT when done  
ENV DEBIAN_FRONTEND noninteractive  
WORKDIR /tmp/  
RUN apt-get --quiet update && \  
apt-get --quiet --yes --force-yes upgrade && \  
apt-get -y install git apache2 vim libcurl4-openssl-dev libxslt-dev
libxml2-dev \  
libpq-dev apache2-threaded-dev libapr1-dev libaprutil1-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#############Clone webSite
Files###############################################################  
RUN git clone https://github.com/cloud9ers/silicon-vision.git  
RUN /bin/bash -c 'mv /tmp/silicon-vision/* /var/www/html/'  
RUN /bin/bash -c 'chown -R www-data:www-data /var/www/html'  
###### Install rvm, ruby, rubygems, passenger, apache2Module#####  
WORKDIR /var/www/html/  
ENV RUBY_VERSION 2.0.0-p648  
ENV RAILS_VERSION 3.2.13  
ENV PASSENGER_VERSION 5.0.23  
########## Installs and updates
rvm,rail,bundle,gem,passenger,apacheModule#######################  
########cash bundle installation---should done in same dir where app and
"GemFile"is located######  
RUN \curl -L https://get.rvm.io | bash -s head --autolibs=4  
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc  
RUN /bin/bash -l -c 'rvm requirements && rvm install $RUBY_VERSION && rvm use
$RUBY_VERSION --default'  
RUN /bin/bash -l -c 'gem install rails --version=$RAILS_VERSION && gem install
bundler && gem install passenger --version $PASSENGER_VERSION --no-rdoc --no-
ri'  
RUN /bin/bash -l -c 'passenger-install-apache2-module --auto'  
RUN /bin/bash -l -c 'bundle install --jobs 20 --retry 5'  
##################################################################################################  
RUN /bin/bash -c 'usermod -G rvm root'  
RUN /bin/bash -c 'usermod -G www-data root'  
##################################################################################################  
######config-passenger############################################  
RUN echo "LoadModule passenger_module
/usr/local/rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION/buildout/apache2/mod_passenger.so"
> /etc/apache2/mods-available/passenger.load  
  
RUN echo "<IfModule mod_passenger.c>\n \  
PassengerRoot
/usr/local/rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION\n \  
PassengerDefaultRuby /usr/local/rvm/gems/ruby-$RUBY_VERSION/wrappers/ruby\n \  
</IfModule>" > /etc/apache2/mods-available/passenger.conf  
  
RUN echo "<IfModule mod_passenger.c>\n \  
PassengerRoot
/usr/local/rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION\n \  
PassengerDefaultRuby /usr/local/rvm/gems/ruby-$RUBY_VERSION/wrappers/ruby\n \  
</IfModule>" >> /etc/apache2/apache2.conf  
  
RUN a2enmod passenger  
RUN a2enmod rewrite  
####################Virtual Host####################################  
RUN echo "<VirtualHost *:80>\n \  
ServerName example.com\n \  
ServerAlias www.example.com\n \  
ServerAdmin webmaster@localhost\n \  
DocumentRoot /var/www/html/public\n \  
RailsEnv development\n \  
ErrorLog ${APACHE_LOG_DIR}/error.log\n \  
CustomLog ${APACHE_LOG_DIR}/access.log combined\n \  
<Directory "/var/www/html/public">\n \  
Options FollowSymLinks\n \  
Require all granted\n \  
</Directory>\n \  
</VirtualHost>" > /etc/apache2/sites-available/sivi.conf  
####################################################################  
RUN a2ensite sivi  
RUN a2dissite 000-default  
EXPOSE 80  
ENTRYPOINT apache2ctl -D FOREGROUND  

