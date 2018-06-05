From grahamc/jekyll  
MAINTAINER jon.weisz@gmail.com  
  
RUN apt-get update && apt-get install bundler -y  
  
RUN apt-get update  
RUN apt-get install -y curl git build-essential ruby1.9.1 libsqlite3-dev  
RUN gem install rubygems-update --no-ri --no-rdoc  
RUN update_rubygems  
RUN gem install bundler --no-ri --no-rdoc  
  
VOLUME /src  
  
ONBUILD WORKDIR /tmp  
ONBUILD ADD Gemfile Gemfile  
ONBUILD ADD Gemfile.lock Gemfile.lock  
ONBUILD RUN bundle install  
  
ONBUILD WORKDIR /src  
ONBUILD ENTRYPOINT ["/bin/sh", "-c"]  
ONBUILD CMD ["bundle exec jekyll serve --port 4000 --host 0.0.0.0"]  

