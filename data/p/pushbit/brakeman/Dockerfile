FROM pushbit/ruby  
  
RUN gem install brakeman  
RUN gem install faraday  
  
ADD ./execute.sh ./execute.sh  
ADD ./execute.rb ./execute.rb  
  
CMD ["./execute.sh"]

