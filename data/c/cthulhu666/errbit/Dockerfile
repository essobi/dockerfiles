FROM ruby:2.3.1-slim  
MAINTAINER jakub.gluszecki@gmail.com  
  
RUN apt-get -qq update -y && \  
apt-get -qq install -y build-essential curl  
RUN gem install foreman --no-ri  
RUN mkdir /app && cd /app && curl
https://codeload.github.com/errbit/errbit/tar.gz/v0.6.1 | tar xz && ln -s
errbit-0.6.1 errbit  
  
WORKDIR /app/errbit  
RUN bundle install --without test development  
RUN bundle exec rake assets:precompile  
  
ENV RAILS_ENV production  
ENV PORT 3000  
EXPOSE 3000  
CMD foreman start -f Procfile  
  

