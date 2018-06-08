FROM ruby:2.0  
# Update and upgrade  
RUN apt-get update && apt-get upgrade -y  
  
# Install phantomjs for feature testing  
ENV PHANTOMJS_VERSION 1.9.7  
RUN \  
apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \  
apt-get autoremove -y  
  
# Install Nodejs  
RUN apt-get install -y nodejs --no-install-recommends  
  
# see http://guides.rubyonrails.org/command_line.html#rails-dbconsole  
RUN apt-get install -y mysql-client postgresql-client sqlite3 --no-install-
recommends  
RUN rm -rf /var/lib/apt/lists/*  
  
# Cleanup  
RUN apt-get clean all  
  
# Configure Bundler  
RUN bundle config --global frozen 1  
RUN bundle config --global jobs `nproc`  

