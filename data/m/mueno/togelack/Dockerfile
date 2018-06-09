FROM ruby:2.2.4-onbuild  
MAINTAINER m-ueno (https://github.com/m-ueno/)  
  
ENV BUNDLE_JOBS=4 \  
BUNDLE_FROZEN=1  
ENV PORT=3000  
EXPOSE 3000  
RUN bundle exec rake assets:precompile RAILS_ENV=production  
CMD bundle exec puma -C config/puma.rb  
  

