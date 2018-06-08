FROM ruby:2.2  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY packages /usr/src/app/  
ONBUILD RUN /bin/bash -c "apt-get update && apt-get install -y \$(cat
packages) --no-install-recommends && rm -rf /var/lib/apt/lists/*"  
  
ONBUILD COPY Gemfile /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle install  
  
ONBUILD COPY . /usr/src/app  
  
EXPOSE 9292  
CMD [ "rackup", "-o", "0.0.0.0" ]  

