# Base image  
FROM ruby:latest  
  
ENV HOME /home/rails/webapp  
  
# Install PGsql dependencies and js engine  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
  
WORKDIR $HOME  
# Install gems  
ADD Gemfile* $HOME/  
RUN bundle install --without test  
  
# Add the app code  
ADD . $HOME  
  
# ENV RAILS_ENV=production  
ENV APP_USER_POSTGRES_PASSWORD=ruby  
ENV
SECRET_KEY_BASE=cf46bf2bb2156bba631dc0110335daa037c1d7636f30bf5107dd06ae0076be76dac7d603e9d08f21930c64953d1699ed22fea2606788252b6745e68113dab691  
  
EXPOSE 3000  
# RUN rake db:create && rake db:migrate  
# Default command  
CMD ["rails", "server", "--binding", "0.0.0.0", "-p", "3000"]

