FROM ruby:2.2.4  
  
MAINTAINER benjamin.meichsner@aboutsource.net  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
mysql-client \  
postgresql-client \  
nodejs \  
xvfb && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
RUN cd /tmp && \  
curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
| \  
tar xj phantomjs-1.9.8-linux-x86_64/bin/phantomjs && \  
cp phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin && \  
rm -rf phantomjs*  

