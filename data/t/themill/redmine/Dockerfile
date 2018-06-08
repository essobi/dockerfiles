FROM redmine:3.4  
COPY plugins/ /usr/src/redmine/plugins/  
  
COPY themes/ /usr/src/redmine/public/themes/  
  
COPY configuration.yml /usr/src/redmine/config/configuration.yml  
  
COPY repo_fetch.cron /etc/cron.d/repo_fetch  
RUN chmod 0644 /etc/cron.d/repo_fetch

