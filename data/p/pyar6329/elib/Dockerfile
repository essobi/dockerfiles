FROM rails:onbuild  
RUN rake db:migrate:reset db:seed  
CMD ["rails", "s", "-b", "0.0.0.0"]  

