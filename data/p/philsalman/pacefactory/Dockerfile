############################  
# Grab Ubuntu Base Image #  
############################  
FROM ubuntu:xenial  
SHELL ["/bin/bash", "-c"]  
MAINTAINER David Salman  
  
########################  
# Setup Environments #  
########################  
ENV DEBIAN_FRONTEND noninteractive  
ENV SERVER_IP 127.0.0.1  
  
####################################  
# Apache Web Server Installation #  
####################################  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y apache2  
  
#################################  
# Configure Apache Web Server #  
#################################  
RUN apt-get install -y iproute2 ufw  
RUN export SERVER_IP=$(ip addr show lo | grep inet | awk '{ print $2; }' | sed
's/\/.*$//')  
RUN echo "ServerName $SERVER_IP" >> etc/apache2/apache2.conf  
  
RUN ufw app list && \  
ufw app info "Apache Full"  
#ufw allow in "Apache Full"  
  
RUN mkdir -p /var/www/PaceFactory/dist  
RUN chmod -R 755 /var/www  
  
RUN touch /etc/apache2/sites-available/pacefactory.com.conf  
RUN echo -e \  
"<VirtualHost *:80>\n\t\  
ServerAdmin dev@pacefactory.com\n\t\  
ServerName pacefactory.com\n\t\  
ServerAlias www.pacefactory.com\n\t\  
DocumentRoot /var/www/PaceFactory/dist\n\t\  
ErrorLog ${APACHE_LOG_DIR}/pacefactory-error.log\n\t\  
CustomLog ${APACHE_LOG_DIR}/pacefactory-access.log combined\n\  
</VirtualHost>" \  
>> /etc/apache2/sites-available/pacefactory.com.conf  
  
RUN a2ensite pacefactory.com.conf  
RUN service apache2 restart  
RUN apachectl configtest  
  
RUN echo -e "$SERVER_IP pacefactoryapi.com" >> /etc/hosts  
  
########################  
# Install NodeJS/NPM #  
########################  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -  
RUN apt-get install -y nodejs build-essential  
RUN npm i -g n  
RUN n 10.0.0  
  
RUN nodejs -v  
RUN npm -v  
  
########################  
# Setup PaceFactory #  
########################  
WORKDIR /var/www/PaceFactory  
COPY package*.json ./  
RUN npm install  
  
COPY . .  
#RUN npm run dev  
  
####################  
# Image Settings #  
####################  
#EXPOSE 80 443 8080  
#VOLUME ["/var/www/PaceFactory"]  
  
##########################  
# Launch Micro-Service #  
##########################  
CMD ["npm", "run", "build"]  

