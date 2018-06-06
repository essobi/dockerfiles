FROM ruby:2.3.2-slim  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
  
WORKDIR /usr/src/app  
  
ADD Gemfile ./  
ADD Gemfile.lock ./  
RUN bundle install  
  
RUN mkdir spec features /results  
COPY spec ./spec/  
COPY features ./features/  
  
COPY run.sh ./  
  
ENTRYPOINT ["./run.sh"]  

