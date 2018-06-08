FROM alpine  
  
RUN apk add --no-cache \  
curl \  
perl \  
perl-switch \  
perl-datetime \  
perl-sys-syslog \  
perl-lwp-protocol-https  
  
RUN curl https://aws-
cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.1.zip |
\  
unzip -  
RUN chmod +x /aws-scripts-mon/mon-put-instance-data.pl  
  
COPY crontab /etc/crontabs/root  
  
CMD [ "crond", "-f", "-d8" ]  

