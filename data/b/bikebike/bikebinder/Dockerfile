##############  
# BikeBinder #  
##############  
# Password is password for staff@freeridepgh.org & volunteer@freeridepgh.org  
  
FROM bikebike/bikebike:16.04  
MAINTAINER Jonathan Rosenbaum <gnuser@gmail.com>  
  
RUN git clone https://github.com/FreeRidePGH/BikeBinder.git  
RUN gem install bundler  
RUN apt-get update && apt-get -y install g++ libfcgi-dev libsqlite3-dev ruby-
sqlite3  
RUN bundle install --gemfile=/BikeBinder/Gemfile  
COPY devise.rb /BikeBinder/config/initializers/  
RUN cd /BikeBinder; bundle exec rake setup; bundle exec rake populate  
  
# setup to use sqlite3  
COPY bikebinder.conf /etc/supervisor/conf.d/  
#COPY /BikeBinder/config/application/mailer_config.rb
/BikeBinder/config/database.yml  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
  
# http://stackoverflow.com/questions/32799856/rails-webrick-server-default-ip-
and-port  
# docker run -d -p 3000:3000 \--name="bikebinder" bikebike/bikebinder  

