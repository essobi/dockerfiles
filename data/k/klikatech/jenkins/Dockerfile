FROM jenkins/jenkins:lts  
  
MAINTAINER Eugene Volchek <evolchek@klika-tech.com>  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y rsync ruby-full apt-utils build-essential gcc ant maven
libssl-dev libappindicator1 libindicator7 libpango1.0-0 fonts-liberation xdg-
utils python3 python-pip jq gconf-service libgconf-2-4 \  
php-common php-dev php-cli php-curl php-memcached php-mysql php-gd \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome*.deb \  
&& apt-get install -y -f \  
&& apt-get install -y xvfb \  
&& wget -N
http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& chmod +x chromedriver \  
&& mv -f chromedriver /usr/local/share/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \  
&& ln -s /usr/local/share/chromedriver /usr/bin/chromedriver \  
&& apt-get install -y nodejs \  
&& npm install -g npm@next \  
&& npm install -g bower \  
&& npm install -g jasmine \  
&& npm install -g grunt-cli \  
&& npm install -g typings \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& gem install sass \  
&& gem install compass \  
&& gem install jekyll \  
&& gem install jekyll-paginate \  
&& gem install --pre sass-css-importer \  
&& pip install awscli \  
&& curl -sSL https://get.docker.com/ | sh \  
&& apt-get -y autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER jenkins  

