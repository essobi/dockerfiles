FROM ubuntu  
MAINTAINER Matt S. Garrison <matt@mattsgarrison.com>  
  
# Disable apt prompts  
ENV DEBIAN_FRONTEND noninteractive  
  
# CREATE USER  
RUN useradd -d /home/deployer -m deployer  
RUN chown -R deployer:deployer /home/deployer  
  
# POSTGRES  
RUN apt-get install -y -q postgresql-9.1  
RUN apt-get install -y -q postgresql-contrib-9.1  
RUN apt-get install -y -q libpq-dev  
# RUBY  
RUN apt-get -y install build-essential git zsh curl wget  
RUN apt-get install -y -q ruby1.9.1 ruby1.9.1-dev rubygems1.9.1 irb1.9.1
build-essential libopenssl-ruby1.9.1 libssl-dev zlib1g-dev  
  
# For execjs - needs node  
RUN apt-get install -y python-software-properties python python-setuptools  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y nodejs vim emacs htop tree zsh fish  
  
### SERVICES ###  
# Supervisor  
RUN apt-get install -y -q supervisor  
  
# MEMCACHED  
RUN apt-get install -y -q memcached  
  
# REDIS for background queues  
RUN apt-get install -y -q redis-server  
  
# MAGICK  
#RUN apt-get install -y -q imagemagick  
#RUN apt-get install -y -q graphicsmagick  
#RUN apt-get install -y -q graphicsmagick-libmagick-dev-compat  
# Install an updated Ruby  
RUN apt-get install -y libyaml-dev ncurses-dev libreadline-dev bison libgdbm-
dev libc6-dev libssl-dev libsqlite3-dev make build-essential libssl-dev
libreadline6-dev zlib1g-dev libyaml-dev libreadline-ruby libopenssl-ruby
libcurl4-openssl-dev libxml2-dev libxslt1-dev libpq-dev gcc  
RUN apt-get install -y ruby2.1 ruby2.1-dev  
  
EXPOSE 3000  
  
#ADD /home/matt/Projects/web/railsgirls_nola /rails_app  
#WORKDIR /rails_app  
#RUN bundle install  
#ENTRYPOINT ["/rails_app"]  
#CMD ["su", "-", "deployer", "/usr/local/bin/passenger", "start",
"/rails_app/"]  
# Set up a default runtime command  
#CMD rails server  
CMD "echo its alive"

