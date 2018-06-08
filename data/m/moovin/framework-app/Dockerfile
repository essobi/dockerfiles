FROM moovin/php:7.0-apache  
  
# Frontend tools  
RUN ((curl -sL https://deb.nodesource.com/setup_7.x | bash) || true) && \  
apt-get install -y \  
nodejs \  
build-essential \  
&& rm -rf /var/cache/apt/archives/*  
  
RUN npm install -g \  
bower \  
grunt \  
grunt-cli \  
typescript \  
gulp-cli  
  
# Apache  
RUN a2enmod rewrite headers  
COPY conf/sites/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
CMD bash -c "ROOT_PATH=\${ROOT_PATH:-/var/www/html} &&
ROOT_PATH=\${ROOT_PATH//\//\\\\\/} \  
&& sed -i \"s/\\\$ROOT_PATH/\$ROOT_PATH/\" /etc/apache2/sites-
enabled/000-default.conf \  
&& apache2-foreground"

