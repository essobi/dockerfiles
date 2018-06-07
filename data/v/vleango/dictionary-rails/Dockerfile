# rails new project_rails -d=postgresql --skip-yarn --skip-git --skip-puma
--skip-action-cable --skip-coffee --skip-turbolinks --skip-test --skip-system-
test --api  
FROM ruby:2.5.0  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
  
# required to be passed in  
ARG APP_PATH  
  
ARG INSTALL_PATH=/app  
ARG LOCAL_USER=rails  
  
# Create a directory where our app will be placed  
RUN mkdir -p $INSTALL_PATH  
  
# Change directory so that our commands run inside this new directory  
WORKDIR $INSTALL_PATH  
  
# Create local user  
RUN useradd -ms /bin/bash $LOCAL_USER  
USER $LOCAL_USER  
  
# Copy dependency definitions  
# IMPORTANT:: Need to turn off if starting new app  
COPY $APP_PATH/Gemfile $INSTALL_PATH/Gemfile  
COPY $APP_PATH/Gemfile.lock $INSTALL_PATH/Gemfile.lock  
RUN bundle install  
  
COPY . $INSTALL_PATH  
  
CMD ["rails", "server"]  

