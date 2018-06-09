FROM jamgood96/alpine-ruby  
  
RUN mkdir -p /web/service  
WORKDIR /web/service  
  
COPY Gemfile /web/service/  
COPY Gemfile.lock /web/service/  
RUN bundle install  
  
COPY . /web/service  
  
EXPOSE 3000  

