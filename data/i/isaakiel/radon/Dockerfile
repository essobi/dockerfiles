FROM ruby:2.3.5-jessie  
MAINTAINER Martin Hinz <martin.hinz@ufg.uni-kiel.de>  
  
# Install nginx with passenger  
RUN gem install passenger -v 5.0.4 && \  
apt-get update && \  
apt-get install -y libcurl4-openssl-dev && \  
apt-get install -y qt4-default && \  
apt-get install -y libqtwebkit-dev && \  
passenger-install-nginx-module --auto  
  
ADD docker/rails/conf/nginx.conf /opt/nginx/conf/nginx.conf  
  
# Add configuration to set daemon mode off  
RUN echo "daemon off;" >> /opt/nginx/conf/nginx.conf  
  
# Install Rails dependencies  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
# Throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
# Set Workdir  
WORKDIR /usr/src/app  
  
# File transfer into container  
RUN mkdir -p .  
ADD Gemfile .  
ADD Gemfile.lock .  
ADD docker/rails/start.sh .  
  
# Bundle install  
RUN bundle install --system  
ADD . .  
  
# Initialize log  
RUN mkdir -p ./log  
RUN cat /dev/null > ./log/production.log  
RUN chmod -R a+w ./log  
  
# Port  
EXPOSE 80  
# Rails Environment  
ENV RAILS_ENV=production  
  
# Permission management  
RUN chmod +x ./start.sh  
RUN mkdir -p ./tmp  
RUN chown -R nobody:nogroup ./tmp  
  
# Define start script  
CMD ["./start.sh"]  

