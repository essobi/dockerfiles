FROM debian  
  
MAINTAINER Giménez Silva Germán Alberto <ggerman@gmail.com>  
  
RUN apt-get update && apt-get install -y patch ruby ruby-dev gcc g++ make
zlib1g-dev vim  
  
RUN gem install mini_portile --no-rdoc --no-ri  
RUN gem install rake --no-rdoc --no-ri  
RUN gem install patch --no-rdoc --no-ri  
RUN gem install bundler pry --no-rdoc --no-ri  
RUN gem install volt --no-rdoc --no-ri  
RUN gem install nokogiri -v '1.6.6.2' \--no-rdoc --no-ri  
  
ENV APP /app  
WORKDIR $APP  
  
RUN volt new . && bundle install  
RUN rm config/app.rb  
COPY app.rb config/app.rb  
  
ENTRYPOINT ["bundle", "exec", "volt", "server"]  
  

