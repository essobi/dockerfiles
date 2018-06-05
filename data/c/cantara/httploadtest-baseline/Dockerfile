FROM cantara/alpine-zulu-jdk8  
MAINTAINER Totto <totto@totto.org>  
  
ENV USER=HTTPLoadTest-baseline  
ENV HOME=/home/$USER  
ENV APP=HTTPLoadTest-baseline  
  
RUN adduser -D -s /bin/sh $USER  
# This application should have a good headroom for threads  
RUN ulimit -Su 62000  
  
RUN apk -Uu add wget logrotate bash  
  
## Set up start of services  
RUN apk -Uu add py-setuptools  
RUN apk -Uu add supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN ln -s /etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/supervisord.conf  
  
## Download scripts  
RUN wget
https://raw.githubusercontent.com/Cantara/devops/master/pull_deploy/linux/build/Docker/application_scripts/start-
service.sh \  
-P $HOME && \  
wget
https://raw.githubusercontent.com/Cantara/devops/master/pull_deploy/linux/build/Docker/application_scripts/stop-
service.sh \  
-P $HOME  
RUN wget
https://raw.githubusercontent.com/Cantara/devops/master/pull_deploy/linux/build/Docker/application_scripts/update-
service.sh \  
-P $HOME  
  
## Configure application  
COPY scripts/* $HOME/  
COPY CRON $HOME/  
RUN chmod 755 $HOME/*.sh  
  
##Directories to persist for data volumes  
RUN mkdir $HOME/logs  
RUN mkdir $HOME/db  
COPY config_override_templates/* $HOME/config_override/  
COPY loadtest_setup/* $HOME/loadtest_setup/  
COPY scripts/* $HOME/  
  
##Configure crontab  
ADD crontab /etc/cron.d/HTTPLoadTest  
RUN chmod 0644 /etc/cron.d/HTTPLoadTest  
RUN touch /var/log/cron.log  
RUN chown $USER /var/log/cron.log  
RUN crontab -u $USER /etc/cron.d/HTTPLoadTest  
  
##Configure logrotate  
COPY logrotate_config/logrotate.conf /etc/logrotate.conf  
COPY logrotate_config/logrotate.d/* /etc/logrotate.d/  
  
#Permissions  
RUN chown -R $USER:$USER $HOME  
  
##Download application  
RUN su - $USER -c $HOME/update-service.sh  
  
RUN ln -s /usr/local/java/bin/java /usr/bin/java  
  
VOLUME ["$HOME/config_override", "$HOME/db", "$HOME/logs"]  
  
EXPOSE 8086  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

