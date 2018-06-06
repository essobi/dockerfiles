FROM ruby:2.2-slim  
MAINTAINER Joe Rocklin <joe.rocklin@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
gcc \  
make \  
patch \  
locales \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY locale.gen /etc/locale.gen  
  
RUN echo 'locales locales/default_environment_locale select en_US.UTF-8' |
debconf-set-selections -v \  
&& rm --force --verbose /etc/default/locale \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG='en_US.UTF-8' \  
&& update-locale LANGUAGE='en_US.UTF-8'  
  
ENV LC_ALL=en_US.UTF-8  
  
RUN gem install bundler --no-ri --no-rdoc \  
&& gem install foodcritic -v 6.3.0 \--no-ri --no-rdoc \  
&& gem install cookstyle --no-ri --no-rdoc \  
&& gem install chefspec -v 4.7.0 \--no-ri --no-rdoc \  
&& gem install chef-sugar -v 3.3.0 \--no-ri --no-rdoc \  
&& gem install berkshelf -v 4.3.5 \--no-ri --no-rdoc  
  

