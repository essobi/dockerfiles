FROM ruby:2.3.1  
COPY Gemfile /usr/src/app/source/Gemfile  
COPY Gemfile.lock /usr/src/app/source/Gemfile.lock  
  
WORKDIR /usr/src/app/source  
RUN gem sources --add https://gems.ruby-china.org/ --remove
https://rubygems.org/ \  
&& gem install bundle \  
&& apt-get update \  
&& apt-get install -y nodejs \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& bundle install  
  
VOLUME /usr/src/app/source  
  
ENTRYPOINT ["bundle"]  

