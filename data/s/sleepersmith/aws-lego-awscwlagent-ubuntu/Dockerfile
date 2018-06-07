FROM ubuntu:14.04.4  
ADD awslogs-agent-setup.py CloudWatchMonitoringScripts-1.2.1.zip default.conf
/home/local/  
RUN apt-get update && \  
apt-get install -y python curl unzip libwww-perl libdatetime-perl  
  
RUN unzip /home/local/CloudWatchMonitoringScripts-1.2.1.zip && \  
rm /home/local/CloudWatchMonitoringScripts-1.2.1.zip  
RUN python /home/local/awslogs-agent-setup.py \  
-r {{aws-region}} \  
-c /home/local/default.conf \  
-n && \  
service awslogs stop  
RUN rm /home/local/awslogs-agent-setup.py && \  
rm /var/log/awslogs.log  
  
VOLUME ["/var/awslogs/state/"]  
  
ADD init.sh /home/local/  
RUN chmod +x /home/local/init.sh  
  
ENTRYPOINT ["/home/local/init.sh"]  

