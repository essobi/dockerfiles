FROM ruby:2.3.1  
RUN apt-get update && apt-get install -qq -y build-essential nodejs --fix-
missing --no-install-recommends  
  
ENV INSTALL_PATH /hate_app  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle  
  
COPY . .  
  
VOLUME ["$INSTALL_PATH/public"]  
  
EXPOSE 3000  
CMD bundle exec rails server -b '0.0.0.0'  

