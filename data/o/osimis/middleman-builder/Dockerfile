#dockerfile with the build tools used to generate the OSIMIS static websites
(mainly ruby, node & middleman)  
FROM ruby:2.2.4  
RUN gem install middleman  
RUN mkdir -p /project  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
VOLUME [ "/usr/local/bundle" ] # bundled gems are installed there, if we want
them to persist and not reinstall them all at each build, we should map this
volume to a host folder  
  
VOLUME [ "/project"]  
WORKDIR /project  
  
CMD export LC_ALL=C.UTF-8 && bundle install && bundle exec middleman build

