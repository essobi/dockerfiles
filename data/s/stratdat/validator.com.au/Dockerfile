FROM ruby:2.3 as builder  
  
# RUN apt-get update -qq && apt-get install -y nodejs  
RUN gem install jekyll  
  
COPY . /build  
  
WORKDIR /build/  
  
RUN bundle install  
  
RUN jekyll build  
  
# Dumped here - potential checks  
#$HOME/.local/bin/html5validator --root ./_deploy  
#bundle exec htmlproofer ./_deploy --disable-external  
#node --version  
#./node_modules/a11y/cli.js --help  
#./node_modules/a11y/cli.js {_site/*.html,_site/**/*.html}  
FROM nginx  
COPY nginx.d/default.conf /etc/nginx/conf.d/default.conf  
COPY \--from=builder /build/_deploy /usr/share/nginx/html  

