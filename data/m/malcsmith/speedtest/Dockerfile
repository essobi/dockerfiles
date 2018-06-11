FROM ubuntu:16.04  
MAINTAINER Malcolm Smith  
  
# Install Supporting Packages  
RUN apt-get -q update && \  
apt-get install -qy curl python wget cron \  
python-mysql.connector python-dev libmysqlclient-dev python-pip && \  
apt-get -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip && pip install MySQL-python  
  
# Grab the fresh version of speedtest  
RUN wget -O /speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-
cli/master/speedtest.py  
RUN chmod +x /speedtest-cli  
  
#copy and prep speedtest  
COPY speedtest.py /speedtest.py  
RUN chmod a+x /speedtest.py  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/speedtest-cron  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/speedtest-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/speedtest.log  
  
# Run the command on container startup  
CMD ["cron", "-f"]  

