FROM mariadb:latest  
  
# backups to Amazon S3  
RUN apt-get update && apt-get install -y s3cmd && apt-get install -y cron &&
rm -rf /var/lib/apt/lists/*  
  
# Create fake chown so docker scripts won't fail on Bluemix (ugly)  
RUN mv /bin/chown /bin/chown.disabled && echo '#!/bin/bash' > /bin/chown &&
echo '/bin/chown.disabled "$@"' >> /bin/chown && echo 'exit 0' >> /bin/chown
&& chmod +x /bin/chown  
  
COPY s3cfg /root/.s3cfg  
  
# entrypoint  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
RUN touch /var/log/cron.log  
  
CMD cron && tail -f /var/log/cron.log  

