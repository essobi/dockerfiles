# Dockerfile for installing and running Nginx  
# Select ubuntu as the base image  
FROM ubuntu  
MAINTAINER M Bintang <halilintar8@yahoo.com>  
  
VOLUME ["/config"]  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
#Set Environment Variable  
ENV NODE_ENV production  
ENV NODE_CONFIG_DIR /src/config  
  
# Install Required Packages  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install curl unzip git wget vim nginx nodejs npm python-
setuptools libkrb5-dev  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN export TERM=xterm  
  
# Setup Nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN sed -i -e"s/# server_tokens off;/server_tokens off;/"
/etc/nginx/nginx.conf  
ADD /config/default.conf /etc/nginx/sites-available/default  
  
# Setup NodeJS Application  
RUN useradd -M node  
ADD /src /src  
RUN chown -R node:node /src  
RUN chown -R node:node /config  
WORKDIR /src  
RUN npm -g update npm  
RUN npm install  
  
# Setup crontab  
RUN apt-get -y install rsyslog  
#ADD cronjob/files/etc/ssl-cron /etc/cron.d/ssl-cron  
ADD cronjob/files/etc/cache-list /etc/cron.d/cache-list  
ADD cronjob/files/etc/cache-list-force /etc/cron.d/cache-list-force  
ADD cronjob/files/etc/codeset /etc/cron.d/codeset  
ADD cronjob/files/etc/pull-cedarlabs /etc/cron.d/pull-cedarlabs  
ADD cronjob/files/etc/push-cedarlabs /etc/cron.d/push-cedarlabs  
#RUN chmod 0644 /etc/cron.d/ssl-cron  
RUN chmod 0644 /etc/cron.d/cache-list  
RUN chmod 0644 /etc/cron.d/cache-list-force  
RUN chmod 0644 /etc/cron.d/codeset  
RUN chmod 0644 /etc/cron.d/pull-cedarlabs  
RUN chmod 0644 /etc/cron.d/push-cedarlabs  
RUN touch /var/log/cron.log  
  
# Run Supervisord  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
RUN /usr/bin/easy_install superlance  
ADD /config/supervisord.conf /etc/supervisord.conf  
  
# Publish port  
EXPOSE 443  
CMD ["/usr/local/bin/supervisord","-n"]  

