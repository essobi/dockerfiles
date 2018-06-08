FROM ruby:2.5.0  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
  
RUN apt-get update && apt-get install -qq -y --no-install-recommends \  
build-essential libpq-dev curl  
  
WORKDIR /app  
COPY . .  
  
RUN bundle install  
  
CMD ["bin/rails", "server", "-e production"]  

