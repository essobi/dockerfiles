FROM ruby  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
RUN mkdir /myapp  
WORKDIR /myapp  
ADD Gemfile /myapp/Gemfile  
RUN bundle install -j8  
EXPOSE 3000  
ADD . /myapp  
CMD ["bundle", "exec", "rails", "s"]  

