FROM phusion/baseimage  
MAINTAINER support@blackvoid.ch  
  
ENV RUBY_VERSION 2.4.0  
ENV GIT_REPO none  
ENV RAILS_ENV production  
ENV RUBY_INSTALL_VERSION 0.6.1  
VOLUME /srv/app  
WORKDIR /srv/app  
EXPOSE 80  
RUN apt-get update && \  
apt-get install -y wget git curl build-essential nginx \  
libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev \  
libpq-dev libmysqlclient-dev  
  
RUN cd /tmp &&\  
wget -O ruby-install-${RUBY_INSTALL_VERSION}.tar.gz
https://github.com/postmodern/ruby-
install/archive/v${RUBY_INSTALL_VERSION}.tar.gz &&\  
tar -xzvf ruby-install-${RUBY_INSTALL_VERSION}.tar.gz &&\  
cd ruby-install-${RUBY_INSTALL_VERSION}/ &&\  
make install  
  
RUN ruby-install ruby ${RUBY_VERSION}  
  
ENV PATH /opt/rubies/ruby-${RUBY_VERSION}/bin:$PATH  
  
RUN gem install bundler unicorn foreman  
ADD unicorn.rb /srv/app/config/unicorn.rb  
ADD Procfile /srv/app/Procfile  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/sites-enabled/default  
  
ONBUILD ADD . /srv/app  
  
RUN cd /srv/app && git init && git remote add origin ${GIT_REPO}  
  
ADD deploy.sh /usr/local/sbin/deploy  
RUN chmod +x /usr/local/sbin/deploy  
RUN /usr/local/sbin/deploy  
  
CMD bundle install --without test development && bundle exec rake
assets:precompile && foreman start -f Procfile  
  

