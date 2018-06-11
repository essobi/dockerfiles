FROM ruby:2.4.0  
RUN apt-get update  
  
RUN mkdir /product_info_fetcher  
  
ADD . /product_info_fetcher  
  
WORKDIR /product_info_fetcher  
  
RUN bundle install  
  
CMD ["ruby", "index.rb"]  
  

