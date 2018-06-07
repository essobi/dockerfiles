FROM ruby:2.5-slim-stretch  
WORKDIR /usr/src/app  
COPY Gemfile* /usr/src/app/  
RUN bundle install  
COPY *.rb /usr/src/app/  
CMD ["bundle", "exec", "ruby", "/usr/src/app/yamsplode.rb", "/in.yaml",
"/out"]  

