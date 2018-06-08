FROM ruby:2.5.1  
RUN \  
apt-get update && apt-get install -y curl\  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash -\  
&& apt-get update && apt-get install -y build-essential libpq-dev nodejs
nodejs imagemagick\  
&& mkdir -p /myapp/public/uploads\  
&& curl https://github.com/mimolabs/mimo-
api/blob/8893c5bc96017b648b4a8d1d83c6fc8f3d6a0d62/public/square-logo.png >
/myapp/public/uploads/square-logo.png\  
&& npm install -g yarn  
  
WORKDIR /myapp  
COPY Gemfile Gemfile.lock /myapp/  
RUN bundle install  
COPY . /myapp  
COPY ./build/puma.rb /myapp/config/puma.rb  
  
EXPOSE 8080  

