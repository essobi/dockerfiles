FROM ruby:2.5-alpine3.7  
  
RUN mkdir -p /var/lib/fakes3/data  
VOLUME /var/lib/fakes3/data  
  
RUN gem install fakes3  
  
ENTRYPOINT ["/usr/local/bundle/bin/fakes3"]  
CMD ["-r", "/var/lib/fakes3/data", "-p", "4569"]  
  
EXPOSE 4569  

