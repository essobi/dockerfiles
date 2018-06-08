FROM ruby:2.3.4  
MAINTAINER Adam Bowen <adamnbowen@gmail.com>  
  
# Set timezone  
RUN echo "America/Chicago" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# General dependencies:  
RUN apt-get update && \  
apt-get install -y \  
nodejs \  
build-essential \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
# Install Postgres client  
RUN touch /etc/apt/sources.list.d/pgdg.list && \  
echo 'deb http://ftp.debian.org/debian jessie-backports main' \  
>> /etc/apt/sources.list.d/pgdg.list && \  
apt-get update && \  
apt-get -t jessie-backports install -y postgresql-client-9.6 \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
# Install phantomjs  
RUN wget -O /tmp/phantomjs.tar.bz2 \  
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar -xjf /tmp/phantomjs.tar.bz2 -C /tmp \  
&& mv /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs \  
/usr/local/bin/phantomjs  
  
# Install headless-chrome  
RUN apt-get update \  
&& apt-get -yf install libxss1 libappindicator1 libindicator7 gconf-service
libasound2 \  
libgconf-2-4 libgtk-3-0 libnspr4 libx11-xcb1 libxtst6 fonts-liberation libnss3
lsb-release xdg-utils \  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome*.deb \  
&& apt-get -yf install xvfb \  
&& apt-get -yf install unzip \  
&& wget -N
http://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& chmod +x chromedriver \  
&& mv -f chromedriver /usr/local/share/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/bin/chromedriver  
  
# Install heroku toolbelt  
RUN wget \  
https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz \  
-O heroku.tar.gz \  
&& mkdir -p /usr/local/lib \  
&& tar -xvzf heroku.tar.gz -C /usr/local/lib \  
&& /usr/local/lib/heroku/install  

