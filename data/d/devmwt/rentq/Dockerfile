FROM ruby:2.3.1  
MAINTAINER developmentmwt@gmail.com  
RUN apt-get update -qq && apt-get install -y \  
build-essential \  
libmagickwand-dev\  
libpq-dev \  
nodejs \  
postgresql-client\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /app  
WORKDIR /app  
COPY Gemfile Gemfile.lock ./  
ENV RAILS_ENV=staging RACK_ENV=staging  
RUN gem install bundler && bundle install --jobs 20 --retry 5 --without
staging test doc  
COPY . ./  
EXPOSE 3000  
ENTRYPOINT ["bundle", "exec"]  
RUN DB_ADAPTER=nulldb rails assets:precompile  
CMD ["puma", "-C", "config/puma.rb"]  
  

