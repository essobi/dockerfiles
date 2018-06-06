FROM ruby  
  
RUN gem install mailcatcher  
  
ENTRYPOINT ["mailcatcher", "-f", "--ip", "0.0.0.0", "--smtp-port", "25", "--
no-quit"]  

