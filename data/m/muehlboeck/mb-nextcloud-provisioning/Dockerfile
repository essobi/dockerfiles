FROM python:slim-jessie  
  
RUN apt-get update && apt-get -y install cron  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/scripts  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
# COPY script  
COPY check_shares.py ./  
  
# Add crontab file in the cron directory  
COPY crontab /etc/cron.d/nextcloud-provisioning  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/nextcloud-provisioning  
  
# Create the log file to be able to run tail  
RUN mkfifo --mode 0666 /var/log/cron.log  
  
RUN sed --regexp-extended --in-place \  
's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' \  
/etc/pam.d/cron  
  
COPY start-cron /usr/sbin  
  
# Run the command on container startup  
CMD ["start-cron"]  
  

