FROM ruby:2.4.1  
ENV RACK_ENV production  
ENV STORE_DIR /store  
RUN mkdir -p /app && mkdir -p /store  
WORKDIR /app  
COPY Gemfile /app/  
COPY Gemfile.lock /app/  
RUN bundle install --without development test  
COPY . /app  
  
EXPOSE 9292  
CMD ["rackup"]  

