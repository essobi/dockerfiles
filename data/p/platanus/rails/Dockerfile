FROM platanus/ruby:2.0.0-p598  
  
MAINTAINER Juan Ignacio Donoso "juan.ignacio@platan.us"  
# Install nodejs for the asset pipeline  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs  
  
RUN npm install -g bower  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY Gemfile /usr/src/app/Gemfile  
ONBUILD COPY Gemfile.lock /usr/src/app/Gemfile.lock  
  
ONBUILD RUN bundle install  
  
ONBUILD COPY . /usr/src/app  
  
ONBUILD RUN bower install --allow-root  
  
ONBUILD RUN rake assets:precompile  
  
EXPOSE 3000  
CMD ["bin/rails", "server", "-b0.0.0.0"]  

