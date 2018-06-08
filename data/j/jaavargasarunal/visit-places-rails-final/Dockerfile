FROM ruby:2.3  
RUN apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists  
  
WORKDIR /usr/src/app  
COPY Gemfile* ./  
RUN bundle install  
COPY . .  
  
EXPOSE 8500  
CMD rails server -b 0.0.0.0  

