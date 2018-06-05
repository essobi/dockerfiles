FROM triangle/ubuntu-saucy-with-ruby-2.0  
MAINTAINER zs <baloghzsof@gmail.com>  
  
# copy redmine (customized where needed)  
ADD redmine-2.4.1 /redmine/  
  
WORKDIR /redmine  
  
RUN chmod +x redmine  
  
# ruby 2.0 with custom gemset  
RUN /bin/bash -l -c "rvm gemset use redmine --create --default"  
  
# install gems  
RUN /bin/bash -l -c "bundle install --without rmagick"  
  
# volume for the plugins  
VOLUME "/redmine/plugins"  
  
RUN mkdir db/sqlite  
  
# volume for the database  
VOLUME "/redmine/db/sqlite"  
  
# database init  
RUN /bin/bash -l -c "./redmine initialize"  
  
EXPOSE 80  

