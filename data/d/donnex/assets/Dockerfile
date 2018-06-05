FROM ubuntu:14.04  
MAINTAINER Daniel Johansson <donnex@donnex.net>  
  
RUN apt-get update && \  
apt-get install -y build-essential libnotify-bin git-core curl software-
properties-common && \  
curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs && \  
apt-add-repository -y ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y ruby2.3 ruby2.3-dev ruby-switch && \  
ruby-switch --set ruby2.3 && \  
gem install sass && \  
gem install compass && \  
gem install breakpoint && \  
npm install -g gulp && \  
npm install -g bower && \  
npm install -g bower-installer && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /gulp  
  
RUN npm install \  
gulp \  
gulp-jshint \  
gulp-compass \  
gulp-autoprefixer \  
gulp-concat \  
gulp-minify-css \  
gulp-notify \  
gulp-uglify \  
gulp-add-src \  
run-sequence \  
jshint-stylish \  
gulp-livereload  
  
RUN useradd -ms /bin/bash assets  
USER assets  
  
ENTRYPOINT ["/usr/bin/gulp"]  

