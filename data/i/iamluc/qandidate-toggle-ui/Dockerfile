FROM iamluc/symfony:7.0  
RUN apt-get update && apt-get install -y \  
npm \  
nodejs-legacy \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY . ./  
  
RUN npm install  
  
RUN chown -R www-data:www-data /var/www/  
  
# Fucking bower !  
USER www-data  
  
RUN node_modules/.bin/bower install  
  
RUN mv app web  
  
USER root  
  
ENV TOGGLE__API_BASE_URL="http://127.0.0.1:8080"  
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh  

