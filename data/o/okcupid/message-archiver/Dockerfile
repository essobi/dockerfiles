FROM razic/bundler  
  
ADD . /okcupid-message-archiver  
  
WORKDIR /okcupid-message-archiver  
  
RUN bundle install --deployment  
  
ENTRYPOINT ["bundle"]  
  
CMD ["exec", "rake"]  

