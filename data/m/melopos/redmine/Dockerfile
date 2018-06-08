FROM melopos/docker-rvm-ruby-1.9.3  
MAINTAINER melopos - info@melopos.com  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install imagemagick libmagickwand-dev libmysql-ruby mysql-client
libmysqlclient-dev git mercurial -y  
  
# Clone Redmine Repo  
RUN git clone https://github.com/redmine/redmine  
  
ADD database.yml redmine/config/database.yml  
ADD Gemfile.local redmine/Gemfile.local  
ADD configuration.yml redmine/config/configuration.yml  
  
RUN /bin/bash -l -c 'cd redmine && RAILS_ENV=production bundle install
--without development test'  
RUN /bin/bash -l -c 'cd redmine && bundle exec rake generate_secret_token'  
RUN /bin/bash -l -c 'cd redmine && RAILS_ENV=production bundle exec rake
db:migrate'  
RUN /bin/bash -l -c 'cd redmine && RAILS_ENV=production REDMINE_LANG=de bundle
exec rake redmine:load_default_data'  
  
ADD run.rb redmine/run.rb  
WORKDIR redmine  
EXPOSE 3000  
CMD /bin/bash -l -c 'ruby run.rb && bundle exec rails s -e production'

