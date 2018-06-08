FROM phusion/baseimage:0.10.0  
ENV TERM="xterm-256color" \  
LC_ALL="en_US.UTF-8" \  
LANG="en_US.UTF-8" \  
APP_NAME="tripleshot-app" \  
COMPOSER_ALLOW_SUPERUSER="1" \  
APP_ENV="production" \  
PATH="$PATH:/tripleshot/vendor/bin:/tripleshot/node_modules/.bin:/tripleshot"  
EXPOSE 80  
CMD /usr/local/bin/bootstrap-web  
  
ADD . /tripleshot-build  
  
RUN /tripleshot-build/tripleshot-packages.sh && \  
/tripleshot-build/tripleshot-setup.sh  
  
WORKDIR /tripleshot  

