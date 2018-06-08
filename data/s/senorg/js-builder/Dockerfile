FROM buildpack-deps:jessie  
  
RUN apt-get update \  
&& curl -sL http://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y --no-install-recommends \  
nodejs \  
ruby \  
ruby-dev \  
&& gem install --no-rdoc --no-ri sass -v 3.4.22 \  
&& gem install --no-rdoc compass \  
&& npm --global config set color false \  
&& npm \--global config set progress false \  
&& npm install -g gulp-cli \  
&& npm cache clean \  
&& rm -rf ~/.cache/ \  
&& rm -rf /var/lib/apt/lists/* \  
&& true  
  
COPY docker-entrypoint.sh /  
WORKDIR /srv/src  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

