from ruby:2.3.0-alpine  
  
RUN gem install fakes3  
  
RUN mkdir /buckets  
  
WORKDIR /buckets  
  
EXPOSE 4567  
CMD ["fakes3", "--root=/buckets", "--port=4567", "-H=localhost"]  

