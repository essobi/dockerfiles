FROM navyproject/drinking_base  
  
ADD . /var/www  
  
RUN bundle install  
  
WORKDIR /var/www  
EXPOSE 9292  
CMD bundle exec rackup faye.ru -s thin -E production  

