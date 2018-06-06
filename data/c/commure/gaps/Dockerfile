FROM phusion/passenger-ruby21:0.9.19  
MAINTAINER Greg Brockman <gdb@stripe.com>  
  
ENV PORT 3500  
ENV DOCKERIZE_VERSION v0.2.0  
EXPOSE 3500  
ADD Gemfile* /gaps/  
RUN cd /gaps && bundle install --path vendor/bundle  
ADD . /gaps  
  
# If you're running a version of docker before .dockerignore  
RUN rm -f /gaps/site.yaml*  
  
RUN chown -R app: /gaps;  
  
RUN curl -k -L
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
-o /tmp/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz; \  
tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz; \  
rm /tmp/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz;  
  
USER app  
  
ENV HOME /home/app  
ENV RACK_ENV production  
  
WORKDIR /gaps  
  
CMD dockerize -wait tcp://mongo:27017 -timeout 300s bin/hk-runner  

