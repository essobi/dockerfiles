FROM twdevops/ruby:2.1  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
ENV RAILS_ENV development  
  
## Add repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12 &&\  
echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main" >
/etc/apt/sources.list.d/nodejs.list &&\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys AC40B2F7 &&\  
echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty main"
> /etc/apt/sources.list.d/passenger.list  
  
## Install dependencies  
RUN \  
apt-get update &&\  
apt-get install -y --no-install-recommends git imagemagick nodejs nginx-extras
passenger uuid-runtime build-essential libxml2-dev libxslt1-dev libsqlite3-dev
libmysqlclient-dev libpq-dev libmagickwand-dev zlib1g-dev &&\  
ruby2.1 -S passenger-config build-native-support &&\  
wget -P /usr/local/bin
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego &&\  
chmod u+x /usr/local/bin/forego  
  
## work dir  
WORKDIR /rapidftr  
  
## Install gems  
ADD app/Gemfile /rapidftr/  
ADD app/Gemfile.lock /rapidftr/  
RUN \  
bundle install --without test cucumber --jobs 4 --path vendor/ &&\  
rm -Rf vendor/ruby/2.1.0/cache  
  
# Install apps  
ADD app/config.ru /rapidftr/  
ADD app/Rakefile /rapidftr/  
ADD app/LICENSE /rapidftr/  
ADD app/app/ /rapidftr/app/  
ADD app/config/ /rapidftr/config/  
ADD app/db/ /rapidftr/db/  
ADD app/lib/ /rapidftr/lib/  
ADD app/public/ /rapidftr/public/  
ADD app/script/ /rapidftr/script/  
ADD app/solr/ /rapidftr/solr/  
ADD app/vendor/ /rapidftr/vendor/  
  
# Config apps  
ADD Procfile /rapidftr/Procfile  
ADD config/couchdb.yml /rapidftr/config/  
ADD config/sunspot.yml /rapidftr/config/  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/site-nginx.conf /etc/nginx/sites-enabled/default  
  
## Exec tasks  
RUN \  
bundle exec rake assets:clobber assets:precompile  
  
## Install scripts  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME ["/rapidftr/"]  
  

