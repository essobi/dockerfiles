# Base image  
FROM ruby:2.3.1  
ENV HOME /home/rails/webapp  
ENV RAILS_ENV production  
  
# Allow APT to communicate over HTTPS  
RUN apt-get update -qq && apt-get install -y apt-transport-https ca-
certificates  
  
#Add passenger repo to sources  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
561F9B9CAC40B2F7 \  
&& echo deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie
main > /etc/apt/sources.list.d/passenger.list  
  
# Install PGsql dependencies,js engine and passenger  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
ghostscript nginx-extras passenger  
  
RUN useradd kronos  
  
WORKDIR $HOME  
  
# Install gems  
COPY Gemfile* $HOME/  
RUN bundle install --without=development test && gem install foreman  
  
# Add the app code  
COPY . $HOME  
  
# Make the app user owner of the app folder  
RUN chown -R kronos $HOME  
  
USER kronos  
  
#Copy docker database.yml  
COPY database_assets_docker.yml /home/rails/webapp/config/database.yml  
  
#Precompile assets  
RUN bundle exec rake assets:precompile  
  
#Copy docker database.yml  
COPY database_docker.yml /home/rails/webapp/config/database.yml  
  
USER root  
  

