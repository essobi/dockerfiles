FROM ruby:2.4.3  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile .  
COPY Gemfile.lock .  
  
RUN bundle install  
  
COPY . .  

