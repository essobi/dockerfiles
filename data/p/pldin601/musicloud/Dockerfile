FROM pldin601/musicloud-image  
  
MAINTAINER Roman Lakhtadyr <roman.lakhtadyr@gmail.com>  
  
ENV PHP_ENV production  
  
WORKDIR /usr/app/  
  
COPY composer.json composer.lock ./  
RUN composer install --no-plugins --no-scripts --no-dev  
  
COPY package.json package-lock.json ./  
RUN npm install  
  
COPY . ./  
RUN npm run gulp && \  
npm run webpack  
  
ARG GIT_CURRENT_COMMIT="<unknown>"  
ENV GIT_CURRENT_COMMIT=${GIT_CURRENT_COMMIT}  
  
COPY cronfile /etc/cron.d/musicloud  
RUN chmod 0644 /etc/cron.d/musicloud  

