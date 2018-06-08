FROM rails:onbuild  
RUN RAILS_ENV=production rake assets:precompile  
  
VOLUME /usr/src/app/public/uploads  

