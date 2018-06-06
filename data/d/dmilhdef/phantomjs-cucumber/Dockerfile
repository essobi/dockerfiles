FROM ruby:2.3.1  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev cmake  
RUN curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar xjvf -  
ENV PATH=/phantomjs-2.1.1-linux-x86_64/bin:$PATH  
RUN mkdir /test  
WORKDIR /test  
ADD Gemfile /test/Gemfile  
ADD Gemfile.lock /test/Gemfile.lock  
RUN bundle install -j 8  

