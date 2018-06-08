#This dockerfile generates a Docker image that contains all necessary
components (except Oracle) to run a Linkcare instance.  
#The image is created from a base image that contains Linckare-WS with all
base software and adds the following components:  
#- Web Client (Ruby on Rails)  
#- Launch script to start all the components:  
# a) Redis server  
# b) Apache service  
# c) Ruby on Rails  
# d) Worker instance (to execute background tasks of Linkcare WS and LC2)  
FROM linkcare/linkcare-ws:2.6.12  
EXPOSE 80 3000  
# *******************************************  
# INSTALL WEB CLIENT  
RUN set -ex && mkdir -p /www/var/ruby  
WORKDIR /var/www/ruby  
  
# Gem dependencies  
ADD ./Gemfile ./  
ADD ./Gemfile.lock ./  
RUN bundle update eventmachine  
RUN bundle update  
  
# NPM dependencies  
ADD ./package.json ./  
RUN npm install  
  
# Add rest of source code  
ADD . ./  
  
# Compile assets  
#RUN bundle exec rake assets:clean  
RUN bundle exec rake assets:precompile  
ENV REDIS redis:6379  
ENV SECRET_KEY_BASE rake secret  
  
# *******************************************  
# CREATE LAUNCH SCRIPT  
RUN echo 127.0.0.1 redis >> /etc/hosts  
RUN { \  
echo "#!/usr/bin/env bash"; \  
echo "# Delete previous server.pid file. It should normally be deleted by
rails,"; \  
echo "# but if something fails and the file exists, rails won't start"; \  
echo "if [ -f /var/www/ruby/tmp/pids/server.pid ]; then"; \  
echo " rm /var/www/ruby/tmp/pids/server.pid"; \  
echo "fi"; \  
echo "if [ -z \$LINKCARE_APP ]; then"; \  
echo " echo \"CONFIGURATION ERROR!!: It is mandatory to establish the
LINKCARE_APP environtment variable\""; \  
echo " echo \"Remember that LINKCARE_APP variable should match the
\\\\\$GLOBALS['APP'] configured for Linkcare-WS\""; \  
echo " exit; "; \  
echo "fi"; \  
echo "echo \"STARTING REDIS\""; \  
echo "redis-server &"; \  
echo "sleep 3"; \  
echo "echo \"STARTING APACHE\""; \  
echo "apache2-foreground &"; \  
echo "sleep 3"; \  
echo "echo \"STARTING RoR\""; \  
echo "./script/rails server Puma -b 0.0.0.0 &"; \  
echo "echo \"STARTING WORKER\""; \  
echo "export QUEUE=\$LINKCARE_APP"; \  
echo "export APP_INCLUDE=/var/www/html/background/init.php"; \  
echo "export PREFIX=\$LINKCARE_APP"; \  
echo "export COUNT=1"; \  
echo "export INTERVAL=5"; \  
echo "export VVERBOSE=0"; \  
echo "php /var/www/html/vendor/chrisboulton/php-resque/resque.php & echo $! >
/var/www/html/tmp/resque.pid &"; \  
echo "echo \"CONTAINER RUNNING. READY TO USE\""; \  
echo "# The next infinite loop is executed only to start a process that does
not end to prevent"; \  
echo "# Docker from stopping the container after exiting this script"; \  
echo "while [ 0 ] ; do sleep 3600; done"; \  
echo "sleep 3600"; \  
} > ./start_services && chmod 755 ./start_services  
  
CMD ["/var/www/ruby/start_services"]  

