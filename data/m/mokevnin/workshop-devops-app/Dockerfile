FROM ruby:2.5.0  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
  
ENV PROJECT_ROOT /usr/src/app  
  
WORKDIR $PROJECT_ROOT  
  
COPY package.json .  
COPY package-lock.json .  
  
RUN npm install  
  
COPY Gemfile .  
COPY Gemfile.lock .  
  
RUN bundle install  
  
COPY . .  
# RUN NODE_ENV=production RAILS_ENV=production bin/rails assets:precompile
--trace  
VOLUME tmp/cache  
  
CMD ["bin/rails", "server"]  

