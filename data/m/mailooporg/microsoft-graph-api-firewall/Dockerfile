# http://crosbymichael.com/dockerfile-best-practices.html  
# https://github.com/wsargent/docker-cheat-sheet  
FROM ruby:2.4.0-onbuild  
ENV
PATH="/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH}"  
ENV LANG="en_US.UTF-8"  
ENV RACK_ENV="production"  
ENV RAILS_ENV="production"  
ENV RAILS_LOG_TO_STDOUT="enabled"  
ENV RAILS_SERVE_STATIC_FILES="enabled"  
EXPOSE 3000  
CMD rails s  

