FROM php:7.1.16  
RUN apt-get update && apt-get install -y libpng-dev libicu-dev libpq-dev  
RUN docker-php-ext-install bcmath gd intl pdo pdo_pgsql zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN curl -o phpunit -sS -L https://phar.phpunit.de/phpunit-7.phar && mv
phpunit /usr/local/bin && chmod +x /usr/local/bin/phpunit  
  
# Install deps for puppeteer  
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2
libcups2 libdbus-1-3 libexpat1 libfontconfig1 \  
libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4
libpango-1.0-0 libpangocairo-1.0-0 \  
libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1
libxext6 libxfixes3 libxi6 \  
libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation
libappindicator1 libnss3 lsb-release \  
xdg-utils wget git  
  
# Install npm for Puppeteer  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y nodejs  
  
WORKDIR /var/www  

