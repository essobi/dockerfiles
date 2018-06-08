FROM google/ruby  
  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN ["/usr/bin/bundle", "install"]  
ADD . /app  
  
CMD ["foreman", "run", "ruby", "mint-exporter.rb"]  

