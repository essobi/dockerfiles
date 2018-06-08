FROM ruby  
  
CMD ["bundle", "exec", "fluentd", "-c", "/etc/fluent/fluent.conf"]  
  
ENV LANG C.UTF-8  
RUN bundle config --global frozen 1 && \  
mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
  
RUN bundle install  

