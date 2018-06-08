FROM ruby:2.3  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
sqlite3 nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
COPY Gemfile* ./  
RUN bundle install  
COPY . .  
  
EXPOSE 3000  
CMD rake db:create db:migrate && rails server -b 0.0.0.0  

