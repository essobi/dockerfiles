FROM ruby:2.1  
RUN apt-get update -qq && apt-get install -y \  
libpq-dev \  
postgresql-client \  
default-jre  
  
RUN mkdir -p /toshi  
WORKDIR /toshi  
  
ADD Gemfile /toshi/  
ADD Gemfile.lock /toshi/  
RUN bundle install  
  
COPY . /toshi  
  
EXPOSE 5000  
CMD ["bundle", "exec", "puma"]  

