FROM ubuntu:trusty  
MAINTAINER dev@rootree.net <rootree-dev>  
  
RUN apt-get update  
  
# Install ruby dependencies  
RUN apt-get install -y wget curl \  
build-essential git git-core \  
zlib1g-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev  
  
RUN apt-get update  
  
# Install ruby-install  
RUN cd /tmp &&\  
wget -O ruby-install-0.6.0.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.6.0.tar.gz &&\  
tar -xzvf ruby-install-0.6.0.tar.gz &&\  
cd ruby-install-0.6.0/ &&\  
make install  
  
# Install MRI Ruby  
RUN ruby-install ruby 2.3.1  
  
# Add Ruby binaries to $PATH  
ENV PATH /opt/rubies/ruby-2.3.1/bin:$PATH  
  
# Add options to gemrc  
RUN echo "install: --no-document\nupdate: --no-document" > ~/.gemrc  
  
# Install bundler  
RUN gem install bundler  
  
RUN apt-get update  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get install -qq -y nodejs  
  
# Intall software-properties-common for add-apt-repository  
RUN apt-get install -qq -y software-properties-common  
  
# Install Rust  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sudo sh -s --
--channel=nightly  
  
# Install Nginx.  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -qq -y nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN chown -R www-data:www-data /var/lib/nginx  
# Add default nginx config  
ADD nginx-sites.conf /etc/nginx/sites-enabled/default  
  
# Install php5 for inicis  
RUN apt-get install -yq php5-cli php5-mcrypt php5-mysql  
RUN php5enmod mcrypt  
  
## Install MySQL(for mysql, mysql2 gem)  
RUN apt-get install -qq -y libmysqlclient-dev  
  
# Install nmatrix  
RUN apt-get install -qq -y libatlas-base-dev  
RUN update-alternatives --set liblapack.so.3 /usr/lib/atlas-
base/atlas/liblapack.so.3  
RUN update-alternatives --set liblapack.so /usr/lib/atlas-
base/atlas/liblapack.so  
RUN update-alternatives --set libblas.so.3 /usr/lib/atlas-
base/atlas/libblas.so.3  
RUN update-alternatives --set libblas.so /usr/lib/atlas-base/atlas/libblas.so  
  
# Hangul Problem  
RUN locale-gen en_US.UTF-8  
RUN echo 'LC_ALL=en_US.UTF-8' > /etc/default/locale  
RUN echo 'LANG=en_US.UTF-8' >> /etc/default/locale  
  
# Install Rails App  
WORKDIR /app  
ONBUILD ADD Gemfile /app/Gemfile  
ONBUILD ADD Gemfile.lock /app/Gemfile.lock  
ONBUILD ADD Gemfile.lock /app/Gemfile.lock  
ONBUILD RUN bundle install --without development test  
ONBUILD ADD package.json /app/package.json  
ONBUILD RUN npm install  
ONBUILD ADD . /app  
ONBUILD RUN bundle exec rake assets:precompile
RDB_URL="mysql://buildtest:buildtest@localhost/buildtest" RAILS_ENV=production  
ONBUILD RUN cd /app && git rev-parse HEAD > public/version.html  
  
# Add default unicorn config  
ADD unicorn.rb /app/config/unicorn.rb  

