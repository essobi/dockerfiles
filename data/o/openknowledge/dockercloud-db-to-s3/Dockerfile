FROM frolvlad/alpine-python2  
  
COPY backup.py /  
COPY crontab /etc/cron.d/do-backup  
  
RUN apk add --update --no-cache libpq wget python-dev postgresql-dev build-
base postgresql dcron ca-certificates  
RUN pip install python-dockercloud psycopg2 s3cmd  
RUN chmod 0644 /etc/cron.d/do-backup  
RUN touch /var/log/cron.log  
  
# Run the command on container startup  
CMD python /backup.py && \  
crond -s /etc/cron.d -b -L /var/log/cron.log && \  
tail -f /var/log/cron.log  

