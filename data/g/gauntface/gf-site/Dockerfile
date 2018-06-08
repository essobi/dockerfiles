FROM ubuntu:15.10  
# Need to be able to use add-apt-repository  
RUN apt-get -y install software-properties-common curl  
  
# Add NGINX Repo  
RUN add-apt-repository ppa:nginx/development  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
  
# Install Dependencies  
RUN apt-get update  
RUN apt-get -y install nodejs nginx php5 php5-fpm php5-mysql php-apc
php5-imagick php5-curl pngcrush build-essential gettext nano  
  
# Prevent PHP version being shared via headers  
RUN sed -i -e "s/expose_php = On/expose_php = Off/g" /etc/php5/fpm/php.ini  
  
# Remove the default Nginx configuration file  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD nginx/gauntface-shared.conf /etc/nginx/gauntface-shared.conf  
ADD nginx/fastcgi-params.tmpl /etc/nginx/fastcgi-params.tmpl  
  
# CMD envsubst < /etc/nginx/sites-available/gauntface.tmpl > /etc/nginx/sites-
available/gauntface.conf && \  
# if [ -f /gauntface/certs/fullchain.pem -a \  
# -f /gauntface/certs/privkey.pem -a \  
# -f /gauntface/certs/dhparam.cert ]; then \  
# ln -s /etc/nginx/sites-available/gauntface.conf /etc/nginx/sites-
enabled/gauntface.conf; \  
# fi && \  
# service php5-fpm start && \  
# nginx -g 'daemon off;'  
CMD envsubst < /etc/nginx/sites-available/gauntface.tmpl > /etc/nginx/sites-
available/gauntface.conf && \  
envsubst < /etc/nginx/fastcgi-params.tmpl > /etc/nginx/fastcgi-params.conf &&
\  
ln -s /etc/nginx/sites-available/gauntface.conf /etc/nginx/sites-
enabled/gauntface.conf && \  
service php5-fpm start && \  
nginx -g 'daemon off;'  

