FROM ruby:2.3  
USER root  
  
ENV BUNDLER_VERSION 1.15.1  
# en - English  
# pt - Portuguese and Brazilian Portuguese  
# es - Spanish  
# pl - Polish  
ENV ASPELL_LANGUAGES aspell-en aspell-pt aspell-es aspell-pl  
  
# JavaScript runtime required by execjs gem  
# Spellchecking  
ENV PACKAGES nodejs aspell $ASPELL_LANGUAGES  
  
RUN apt-get update && apt-get -y install $PACKAGES  
  
# Fix the Bundler version  
RUN gem install bundler -v $BUNDLER_VERSION  
RUN mkdir /src  
  
WORKDIR /src  
  
ADD Gemfile /src/Gemfile  
ADD Gemfile.lock /src/Gemfile.lock  
RUN bundle install  
  
ADD . /src  
  
CMD bundle exec middleman  

