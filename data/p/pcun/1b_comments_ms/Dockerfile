FROM ruby:2.3  
RUN mkdir /comments_ms  
WORKDIR /comments_ms  
  
RUN gem install nokogiri nio4r:'2.3.0' puma:'3.11.3' websocket-driver:'0.6.5'
bson:'4.3.0' byebug:'10.0.0' ffi:'1.9.23'  
  
ADD Gemfile /comments_ms/Gemfile  
ADD Gemfile.lock /comments_ms/Gemfile.lock  
  
RUN bundle install  
ADD . /comments_ms  
  
EXPOSE 3303  

