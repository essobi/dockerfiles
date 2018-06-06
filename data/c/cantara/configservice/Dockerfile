FROM cantara/debian-sid-zulu-jdk8  
MAINTAINER Erik Drolshammer <erik-dev@fjas.no>  
  
ENV USER=configservice  
ENV HOME=/home/$USER  
RUN useradd -d "$HOME" -u 500 -m -s /bin/bash $USER  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
supervisor cron logrotate \  
&& rm -rf /var/lib/apt/lists/*  
  
## Fix for python/supervisor error "ImportError: No module named
pkg_resources"  
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O -
| python  
  
## Set up start of services  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
## Download scripts  
RUN wget
https://raw.githubusercontent.com/Cantara/devops/master/pull_deploy/linux/build/Docker/application_scripts/start-
service.sh \  
-P $HOME && \  
wget
https://raw.githubusercontent.com/Cantara/devops/master/pull_deploy/linux/build/Docker/application_scripts/stop-
service.sh \  
-P $HOME && \  
wget
https://raw.githubusercontent.com/Cantara/devops/master/pull_deploy/linux/build/Docker/application_scripts/update-
service.sh \  
-P $HOME  
  
## Configure application  
#COPY application_scripts/* $HOME/  
COPY CRON $HOME/  
ADD enable-automatic-updates.sh $HOME/  
RUN chmod 755 $HOME/*.sh  
  
##Directories to persist for data volumes  
RUN mkdir $HOME/logs  
RUN mkdir $HOME/db  
COPY config_override_templates/* $HOME/config_override/  
  
##Configure crontab  
ADD crontab /etc/cron.d/configservice  
RUN chmod 0644 /etc/cron.d/configservice  
RUN touch /var/log/cron.log  
RUN chown $USER /var/log/cron.log  
  
##Configure logrotate  
COPY logrotate_config/logrotate.conf /etc/logrotate.conf  
COPY logrotate_config/logrotate.d/* /etc/logrotate.d/  
  
#Permissions  
RUN chown -R $USER:$USER $HOME  
  
##Download application  
RUN su - $USER -c "$HOME/update-service.sh"  
  
VOLUME ["$HOME/config_override", "$HOME/db", "$HOME/logs"]  
  
EXPOSE 8086  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

