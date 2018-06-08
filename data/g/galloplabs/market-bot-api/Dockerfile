FROM ubuntu:14.04  
MAINTAINER Jonathon W. Marshall "jonathon@galloplabs.com"  
RUN apt-get update && apt-get install -y build-essential curl git ruby ruby-
dev libxml2-dev zlib1g-dev  
RUN gem install --no-ri --no-rdoc bundler  
RUN groupadd user && useradd --create-home --home-dir /srv/app -g user user  
  
WORKDIR /srv/app  
  
COPY Gemfile /srv/app/Gemfile  
COPY Gemfile.lock /srv/app/Gemfile.lock  
RUN bundle install  
  
COPY config.ru /srv/app/config.ru  
COPY app.rb /srv/app/app.rb  
  
USER user  
CMD ["bundle", "exec", "rackup"]  
  
EXPOSE 9292  

