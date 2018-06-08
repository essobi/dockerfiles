FROM phusion/baseimage  
  
MAINTAINER ouattchidi@gmail.com  
  
#RUN apk update && apk add ca-certificates && update-ca-certificates && apk
add openssl  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
libffi-dev \  
libssl-dev \  
python \  
wget \  
libmysqlclient-dev \  
python-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
# install pip  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm get-
pip.py  
  
RUN pip install --no-cache-dir MySQL-python mysql-python sql-feed-graphite  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Add crontab file in the cron directory  
RUN (crontab -l 2>/dev/null; echo "* * * * * /usr/local/bin/sql-feed-graphite
>> /var/log/cron.log 2>&1") | crontab -  
  
ADD start.sh .  
  
RUN chmod -v +x start.sh  
  
#SQL queries in *json  
VOLUME /opt/sql-feed-graphite/queries/  
  
# Run the command on container startup  
CMD cron  
  
ENTRYPOINT ["./start.sh"]  

