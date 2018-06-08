FROM ubuntu:16.04  
MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates bzip2 apt-transport-https \  
nginx ssmtp cron supervisor \  
gettext-base libelf1 \  
vim curl ssh git nodejs \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo
"deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && apt-get update && apt-get install yarn &&
rm -rf /var/lib/apt/lists/*  
  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV NODE_VERSION 8.2.1  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir -p /var/www/site  
  
# Install npm stuff  
RUN /usr/bin/npm install -g bower gulp-cli webpack  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Install Confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
WORKDIR /var/www/site  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY confd /etc/confd  
COPY start.sh crons.conf post-merge /root/  
COPY default.conf /etc/nginx/sites-enabled/default  
  
# Add cron job  
RUN crontab /root/crons.conf  
  
# Volumes  
VOLUME /var/www/site  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

