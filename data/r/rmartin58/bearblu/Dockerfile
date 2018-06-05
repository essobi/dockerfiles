FROM ruby:2.5  
MAINTAINER Rick Martin <rick@bearblu.com>  
  
RUN apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists  
  
WORKDIR /bearblu  
COPY Gemfile* ./  
RUN bundle install  
COPY . .  
  
EXPOSE 3001  
CMD rails server -b 0.0.0.0 -p 3001  

