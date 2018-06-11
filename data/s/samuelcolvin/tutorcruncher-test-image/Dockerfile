FROM python:3.6.4  
  
MAINTAINER Samuel Colvin <s@muelcolvin.com>  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -qq update \  
&& apt-get -y install git libjpeg-dev libfreetype6-dev libffi-dev
libsqlite3-dev postgresql-client \  
&& apt-get -y install gettext nodejs yarn \  
&& apt-get -y install -f  

