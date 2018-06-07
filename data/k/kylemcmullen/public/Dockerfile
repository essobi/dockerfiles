FROM ruby:2.3  
# throw errors if Gemfile has been modified since Gemfile.lock  
#RUN bundle config --global frozen 1  
# This should be mounted as a volume for local development?  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN bundle install  
  
EXPOSE 3000  
CMD ["/usr/src/app/entrypoint.sh"]  

