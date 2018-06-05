FROM ruby:2.3.1  
  
# Set the locale  
RUN apt-get update -y \  
&& apt-get install -y \  
locales \  
&& locale-gen en_US.UTF-8  
  
RUN apt-get update -y \  
&& apt-get install -y \  
apt-transport-https \  
build-essential \  
libqt5webkit5-dev \  
memcached \  
qt5-default \  
redis-server \  
software-properties-common \  
xvfb \  
wkhtmltopdf \  
&& apt-get -q clean \  
&& rm -rf /var/lib/apt/lists  
  
RUN add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/ jessie-
pgdg main" \  
&& curl -L https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
\  
&& apt-get update -y \  
&& apt-get install -y \  
postgresql \  
postgresql-contrib  
  
RUN add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt
./" \  
&& curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add - \  
&& apt-get update -y \  
&& apt-get install -y heroku  

