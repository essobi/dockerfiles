FROM rails  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN bundle install \--without=development  
RUN bundle config \--global frozen 1  
  
ENV LANG=en_US.UTF-8  
ENV RACK_ENV=production  
ENV RAILS_ENV=production  
ENV PORT=80  
  
EXPOSE 80  
CMD ["foreman", "start"]  
  
# Workaround of https://github.com/bundler/bundler/issues/4576  
RUN gem install bundler  

