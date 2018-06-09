FROM ruby  
RUN gem install sinatra  
RUN gem install thin  
RUN gem install rack-test  
RUN gem install rspec  
RUN gem install json  
RUN gem install sinatra-reloader  
RUN gem install mongoid  
RUN gem install database_cleaner  
RUN mkdir /datasource_manager  
WORKDIR /datasource_manager  
ADD . /datasource_manager  
CMD ["ruby", "/datasource_manager/src/app.rb"]  
EXPOSE 80  

