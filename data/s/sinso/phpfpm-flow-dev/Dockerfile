FROM sinso/phpfpm-flow:5.5  
MAINTAINER Aslam Idrisov <aslambek.idrisov1@swisscom.com>  
  
  
# Install nodejs, npm and install latest version of nodejs  
RUN apt-get update \  
&& apt-get install -y \  
nodejs \  
npm \  
&& rm -r /var/lib/apt/lists/* \  
&& npm install -g n \  
&& n stable  
  
  
  
# install rubygems for compass  
RUN apt-get update \  
&& apt-get install -y \  
ruby-dev \  
rubygems \  
&& rm -r /var/lib/apt/lists/*  
# install our stuff  
RUN \  
npm install -g grunt-cli \  
&& gem install compass \  
&& npm install -g gulp \  
&& npm install -g bower \  
&& npm install -g yo  
  
  
# install composer  
RUN \  
curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# install fontforge and ttfautohint for grunt-webfont  
RUN apt-get update \  
&& apt-get install -y \  
fontforge \  
ttfautohint \  
&& rm -r /var/lib/apt/lists/*  

