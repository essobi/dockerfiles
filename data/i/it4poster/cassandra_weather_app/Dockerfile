FROM cassandra:3.10  
# BASED ON debian:jessie-backports  
RUN apt-get update && apt-get install -y jq curl cron vim && apt-get clean &&
\  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* /var/tmp/*  
  
RUN mkdir /root/input  
RUN mkdir /root/RAM  
#COPY *.txt /root/input/  
COPY *.sh /root/  
COPY *.cql /root/  
RUN chmod +x /root/*.sh  
  
# Add crontab file in the cron directory  
ADD crontab_update /etc/cron.d/crontab_update  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/crontab_update  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Run the command on container startup  
#RUN pip install cassandra-driver && pip install cqlsh && export
CQLSH_NO_BUNDLED=true  
# cassandra via pip doesn't work as expected - issues to load data  
CMD /root/startWeather.sh > /root/start_log.txt && cron && tail -f /dev/null  

