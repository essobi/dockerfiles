FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get install -y python-software-properties software-properties-common  
RUN add-apt-repository -y ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN apt-get install -y imagemagick nginx ruby2.2 ruby2.2-dev nodejs sqlite3
libsqlite3-dev zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-
dev libxml2-dev libxslt1-dev libcurl4-openssl-dev git-core curl phantomjs  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN mkdir -p /var/www  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  

