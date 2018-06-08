FROM debian:jessie  
MAINTAINER rerofumi  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update; \  
apt-get -y upgrade; \  
apt-get -y install build-essential patch \  
zlib1g-dev liblzma-dev libgmp-dev libxml2-dev libxslt1-dev \  
ruby ruby-dev nodejs git \  
libpq-dev libsqlite3-dev sqlite3; \  
gem install rake bundler --no-doc; \  
gem install rails --no-doc -v "= 4.0.0"; \  
cd /root; git clone https://github.com/nabehiro/ore-no-igoogle.git; \  
cd /root/ore-no-igoogle; bundle install; \  
cd /root/ore-no-igoogle; bundle exec rake db:migrate; \  
apt-get -y remove build-essential; \  
apt-get -y autoremove; \  
rm -rf /var/lib/apt/lists/*  
  
RUN cp /root/ore-no-igoogle/config/initializers/omniauth.rb.example /root/ore-
no-igoogle/config/initializers/omniauth.rb  
RUN cp /root/ore-no-igoogle/config/initializers/secret_token.rb.example
/root/ore-no-igoogle/config/initializers/secret_token.rb  
RUN cd /root/ore-no-igoogle; sed -i -e "s/< enter secret token >/`bundle exec
rake secret`/" /root/ore-no-igoogle/config/initializers/secret_token.rb  
  
EXPOSE 8080  
WORKDIR /root/ore-no-igoogle  
  
CMD ["rails","s","-p","8080"]  

