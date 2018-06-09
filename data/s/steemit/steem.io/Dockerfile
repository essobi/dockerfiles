FROM ruby:2.3  
RUN apt-get update -qq && apt-get install -y build-essential git nodejs nginx
gettext  
RUN apt-get clean  
  
ADD contrib/startservices.sh /usr/bin/startservices.sh  
RUN chmod +x /usr/bin/startservices.sh  
ADD contrib/site.conf.template /etc/nginx/site.conf.template  
ADD contrib/nginx.conf.template /etc/nginx/nginx.conf.template  
  
ENV APP_HOME /app  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD Gemfile* $APP_HOME/  
RUN bundle install  
ADD . $APP_HOME  
  
EXPOSE 8080  
# entrypoint / cmd  
CMD /usr/bin/startservices.sh  

