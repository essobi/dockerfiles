FROM ruby:2.3.1  
RUN apt-get update  
  
RUN mkdir /aws_ecommerce_service  
  
ADD . /aws_ecommerce_service  
  
WORKDIR /aws_ecommerce_service  
  
RUN bundle install  
  
CMD ["ruby", "index.rb"]  

