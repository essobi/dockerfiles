FROM ruby:2.3.1  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install
-y nodejs  
  
COPY Gemfile /cache/Gemfile  
COPY Gemfile.lock /cache/Gemfile.lock  
  
RUN cd /cache && bundle install  
  
RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgia/ci-
report-tool/master/dist/framgia-ci && chmod +x /usr/bin/framgia-ci  

