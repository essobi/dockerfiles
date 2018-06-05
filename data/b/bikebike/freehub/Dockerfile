###########  
# FreeHub #  
###########  
# Password is test for greeter, sfbk, mechanic, scbc, cbi, admin  
FROM bikebike/bikebike  
MAINTAINER Jonathan Rosenbaum <gnuser@gmail.com>  
  
RUN git clone git://github.com/asalant/freehub.git  
RUN gem install bundler  
#RUN apt-get -y install ruby-dev  
RUN bundle install --gemfile=/freehub/Gemfile  
RUN service mysql start; cd /freehub; rake db:create:all; rake db:migrate;
rake db:fixtures:load  
  
COPY mysql.conf /etc/supervisor/conf.d/  
COPY freehub.conf /etc/supervisor/conf.d/  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
  
# docker run -d -p 3000:3000 --name="freehub" bikebike/freehub  

