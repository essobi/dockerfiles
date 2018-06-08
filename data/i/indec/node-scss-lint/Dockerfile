FROM node:6-alpine  
MAINTAINER navarroaxel <navarroaxel@gmail.com>  
  
LABEL Description="Node LTS with Ruby installed for scss_lint"  
  
# SCSS-Lint installation  
RUN apk update && apk --update add ruby ca-certificates \  
&& echo 'gem: --no-document' > /etc/gemrc \  
&& gem install scss_lint  

