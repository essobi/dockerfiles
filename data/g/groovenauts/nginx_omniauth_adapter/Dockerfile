FROM ruby:2.3.6  
LABEL maintainer "YAMADA Tsuyoshi <tsu-yamada@groovenauts.jp>"  
  
WORKDIR /usr/src/app  
ADD Gemfile* /usr/src/app/  
RUN bundle install --jobs=4 --without test:development  
RUN cp `bundle show nginx_omniauth_adapter`/config.ru .  
  
ENV RACK_ENV=production  
EXPOSE 8080  
CMD ["bundle", "exec", "rackup", "-p", "8080", "-o", "0.0.0.0", "-s", "puma",
"-O", "Verbose", "config.ru"]  
  

