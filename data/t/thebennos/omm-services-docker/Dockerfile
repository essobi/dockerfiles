FROM webdevops/php-nginx:7.2  
# Environment Variables  
MAINTAINER Benjamin Wenderoth <b.wenderoth@gmail.com>  
RUN apt-get install -y wget curl git supervisor  
RUN apt-get -y install cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Clone our private GitHub Repository  
# repo = https://github.com/thebennos/omm_dataworker.git  
# RUN git clone -b helpdesk3
https://e07a15e5635c022ec7492ffa493a21e863705af3:x-oauth-
basic@github.com:thebennos/OMM-services.git /application/code  
RUN git clone -b files
https://e07a15e5635c022ec7492ffa493a21e863705af3:x-oauth-
basic@github.com/thebennos/OMM-services.git /application/files  
# RUN git clone -b helpdesk3
https://e07a15e5635c022ec7492ffa493a21e863705af3:x-oauth-
basic@github.com:thebennos/OMM-services.git /application/code  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD files-sites.conf /etc/nginx/vhost.common.d/files-sites.conf  
WORKDIR /application/files  
# Setup cron job  
#RUN (crontab -l ; echo "* * * * * echo "Hello world" >> /var/log/cron.log") |
crontab  
#  
RUN (crontab -l ; echo "0 0 * * * php
/application/files/install/admin/tasks/auto_prune.cron.php >> /dev/null 2>&1")
| crontab  
RUN (crontab -l ; echo "0 0 * * * php
/application/files/install/admin/tasks/create_internal_notifications.cron.php
>> /dev/null 2>&1") | crontab  
RUN (crontab -l ; echo "0 * * * * php
/application/files/install/admin/tasks/delete_redundant_files.cron.php >>
/dev/null 2>&1") | crontab  
RUN (crontab -l ; echo "0 0 * * * php
/application/files/install/admin/tasks/downgrade_accounts.cron.php >>
/dev/null 2>&1") | crontab  
RUN (crontab -l ; echo "*/5 * * * * php
/application/files/install/admin/tasks/process_file_queue.cron.php >>
/dev/null 2>&1") | crontab  
RUN (crontab -l ; echo "0 1 * * * php
/application/files/install/admin/tasks/create_email_notifications.cron.php >>
/dev/null 2>&1") | crontab  
  
RUN chown -R application:application /application/files  
RUN chmod 755 /application/files/files  
RUN chmod 755 /application/files/plugins  
RUN chmod 755 /application/files/core/logs  
RUN chmod 755 /application/files/core/cache  
RUN chmod 755 /application/files/_config.inc.php  
  
# Run the command on container startup  
#CMD cron && tail -f /var/log/cron.log  

