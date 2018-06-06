FROM ruby:2.1  
RUN apt-get update && apt-get install -y node  
  
RUN git clone https://github.com/kcruby/newkcruby.git  
WORKDIR newkcruby  
  
RUN bundle install  
  
RUN rm config/database.yml  
RUN echo 'production:' > config/database.yml  
RUN echo ' adapter: postgresql' >> config/database.yml  
RUN echo ' encoding: unicode' >> config/database.yml  
RUN echo " host: <%= ENV['POSTGRES_PORT_5432_TCP_ADDR'] %>" >>
config/database.yml  
RUN echo " port: <%= ENV['POSTGRES_PORT_5432_TCP_PORT'] %>" >>
config/database.yml  
RUN echo ' database: kcruby_production' >> config/database.yml  
RUN echo ' pool: 5' >> config/database.yml  
RUN echo ' username: postgres' >> config/database.yml  
RUN echo ' password: postgres' >> config/database.yml  
  
ENV RAILS_ENV production  
ENV RACK_ENV production  
  
  
CMD ["bundle", "exec", "rails", "server"]  

