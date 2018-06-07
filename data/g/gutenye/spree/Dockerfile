FROM ruby  
  
#RUN sed -i s/deb.debian.org/ftp.cn.debian.org/g /etc/apt/sources.list  
# nodejs for execjs runtime  
# mysql-client for mysqldump  
RUN apt-get update && apt-get install -yq git nodejs imagemagick \  
libsqlite3-dev sqlite3 \  
libmysqlclient-dev mysql-client  
# libpq-dev  
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc  
#RUN gem sources --remove https://rubygems.org/ && gem sources -a
http://mirrors.aliyun.com/rubygems/  
RUN gem install rails -v 5.0.2  
RUN rails _5.0.2_ new /app --skip-bundl  
  
WORKDIR /app  
  
#RUN sed -i "1s~.*~source 'http://mirrors.aliyun.com/rubygems'~" Gemfile  
RUN echo "gem 'spree', '~> 3.2.0'" >> Gemfile  
RUN echo "gem 'spree_auth_devise', '~> 3.2.0.beta'" >> Gemfile  
RUN echo "gem 'spree_gateway', '~> 3.2.0.beta'" >> Gemfile  
RUN echo "gem 'mysql2', '~> 0.4.5'" >> Gemfile  
  
RUN bin/bundle install  
  
# use sqlite3 to install js files, for spree:install needs connect to db  
RUN rails g spree:install --migrate=false \--sample=false \--seed=false  
RUN bundle exec rake railties:install:migrations  
  
EXPOSE 80  
ENTRYPOINT [ "bin/bundle", "exec" ]  
  
CMD [ "rails", "server", "-b", "0.0.0.0", "-p", "80" ]  
# -e production  

