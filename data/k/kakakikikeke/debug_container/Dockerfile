FROM ruby  
  
ADD . /home  
WORKDIR /home  
RUN bundle install --path vendor  
EXPOSE 4567  
CMD ["bundle", "exec", "ruby", "app.rb"]

