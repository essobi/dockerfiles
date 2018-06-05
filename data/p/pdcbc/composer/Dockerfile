# Dockerfile for the PDC's Composer service  
#  
#  
# Composer for aggregate data queries. Links to ComposerDb.  
#  
# Example:  
# sudo docker pull healthdatacoalition/composer  
# sudo docker run -d --name=composer -h composer --restart=always \  
# --link composerdb:database \  
# -p 2774:22 \  
# -p 3002:3002 \  
# -v </path/>/composer:/config:rw \  
# healthdatacoalition/composer  
#  
# Linked containers  
# - Mongo database: --link composerdb:database  
#  
# External ports  
# - AutoSSH: -p <hostPort>:22  
# - Web UI: -p <hostPort>:3002  
#  
# Folder paths  
# - config: -v </path/>:/config/:rw  
#  
#  
FROM phusion/passenger-ruby19  
MAINTAINER derek.roberts@gmail.com  
  
  
# Environment variables  
#  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# SSH config  
#  
RUN rm -f /etc/service/sshd/down; \  
sed -i \  
-e 's/#HostKey \/etc/HostKey \/config/' \  
-e 's/^#AuthorizedKeysFile.*/AuthorizedKeysFile\t\/config\/authorized_keys/' \  
/etc/ssh/sshd_config; \  
( \  
echo ''; \  
echo '# Keep connections alive, 60 second interval'; \  
echo '# '; \  
echo 'Host *'; \  
echo 'ServerAliveInterval 60'; \  
) | tee -a /etc/ssh/ssh_config  
  
# Add user for autossh tunnel  
#  
RUN adduser --quiet --disabled-password --home /home/autossh autossh 2>&1  
  
# Prepare /app/ folder  
#  
WORKDIR /app/  
COPY . .  
RUN sed -i -e 's/localhost:27017/database:27017/' config/mongoid.yml; \  
chown -R app:app /app/; \  
/sbin/setuser app bundle install --path vendor/bundle  
  
# Create startup script and make it executable  
#  
RUN SRV=rails; \  
mkdir -p /etc/service/${SRV}/; \  
( \  
echo '#!/bin/bash'; \  
echo ''; \  
echo ''; \  
echo '# Start service'; \  
echo '#'; \  
echo 'cd /app/'; \  
echo 'exec /sbin/setuser app bundle exec rails server -p 3002'; \  
) \  
>> /etc/service/${SRV}/run; \  
chmod +x /etc/service/${SRV}/run  
  
# Support script for delayed_job and ssh-keygen  
#  
RUN SRV=support; \  
mkdir -p /etc/service/${SRV}/; \  
( \  
echo '#!/bin/bash'; \  
echo ''; \  
echo ''; \  
echo '# Create RSA key if not present'; \  
echo 'if [ ! -s /config/job_params.json ]'; \  
echo 'then'; \  
echo ' ('; \  
echo ' echo -e '"'"'{'"'"; \  
echo ' echo -e '"'"'\t"username": "maintenance",'"'"; \  
echo ' echo -e '"'"'\t"endpoint_names": [ "00" ],'"'"; \  
echo ' echo -e '"'"'\t"query_titles": [ "HDC-0001" ]'"'"; \  
echo ' echo -e '"'"'}'"'"; \  
echo ' ) \'; \  
echo ' > /config/job_params.json'; \  
echo 'fi'; \  
echo ''; \  
echo ''; \  
echo '# Create job_params if not present'; \  
echo 'if [ ! -s /config/ssh_host_rsa_key ]'; \  
echo 'then'; \  
echo ' ssh-keygen -b 4096 -t rsa -f /config/ssh_host_rsa_key -q -N ""'; \  
echo 'fi'; \  
echo ''; \  
echo ''; \  
echo '# Start delayed job'; \  
echo '#'; \  
echo 'cd /app/'; \  
echo 'rm /app/tmp/pids/server.pid > /dev/null'; \  
echo 'exec /sbin/setuser app bundle exec /app/script/delayed_job run'; \  
echo '/sbin/setuser app bundle exec /app/script/delayed_job stop > /dev/null';
\  
) \  
>> /etc/service/${SRV}/run; \  
chmod +x /etc/service/${SRV}/run  
  
# Batch query scheduling in cron  
#  
RUN ( \  
echo '# Run batch queries (23 PST = 7 UTC)'; \  
echo '0 7 * * * /app/util/run_batch_queries.sh'; \  
) \  
| crontab -  
  
# Run Command  
#  
CMD ["/sbin/my_init"]  
  
# Ports and volumes  
#  
EXPOSE 2774 3002  
VOLUME /config  

