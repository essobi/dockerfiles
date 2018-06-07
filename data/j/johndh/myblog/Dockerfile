FROM nginx:stable  
RUN apt update && apt -y upgrade && apt -y install git-core curl zlib1g-dev
build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev libcurl4-openssl-dev libffi-dev rubygems ruby-dev  
RUN apt-get install -qy curl ca-certificates gnupg2 build-essential --no-
install-recommends && apt-get clean  
  
RUN mkdir -p /usr/jekyll  
ADD . /usr/jekyll  
  
RUN ruby -v  
RUN gem install bundler  
WORKDIR "/usr/jekyll"  
  
RUN rm _config.yml  
RUN mv _config.yml.prod _config.yml  
  
RUN bundle config --global silence_root_warning 1  
RUN bundle install  
RUN bundle exec jekyll build  
  
RUN cp -r /usr/jekyll/_site/* /usr/share/nginx/html/

