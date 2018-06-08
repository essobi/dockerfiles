FROM ruby:2.4.1  
ENV LANG=C.UTF-8  
RUN apt-get update -qq && apt-get install -y \  
apt-transport-https  
  
# Add yarn to apt  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Node (yarn needs it)  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Install stuff  
RUN apt-get update -qq && apt-get install -y \  
nodejs \  
yarn  
  
RUN mkdir /app  
WORKDIR /app  
COPY Gemfile* /app/  
RUN gem install bundler  
RUN bundle install  
  
COPY package.json /app/  
COPY yarn.lock /app/  
RUN yarn  
  
COPY . /app  
  
EXPOSE 9292  
CMD ["rackup", "-o", "0.0.0.0"]  

