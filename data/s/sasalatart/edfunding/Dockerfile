FROM rails:onbuild  
MAINTAINER El Escram  
  
ENV RAILS_ENV production  
  
RUN apt-get update && apt-get install imagemagick -y  
RUN bundle exec rake assets:precompile  
  
EXPOSE 3000  

