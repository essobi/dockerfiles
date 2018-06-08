FROM ruby:2.3.5-jessie  
  
COPY phantomjs_1.9.7-0~ppa1_amd64.deb /tmp  
RUN dpkg -i /tmp/phantomjs_1.9.7-0~ppa1_amd64.deb  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY . /usr/src/app  
ENTRYPOINT ["bundle", "exec"]  
CMD ["rake"]  

