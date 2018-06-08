FROM alpine  
MAINTAINER Minoru Nakata <minoru@sprocket.bz>  
  
ARG VERSION=1.2.1  
RUN apk --no-cache --no-progress add coreutils perl perl-datetime perl-lwp-
protocol-https perl-uri \  
&& wget -q http://aws-
cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-${VERSION}.zip
\  
&& unzip CloudWatchMonitoringScripts-${VERSION}.zip \  
&& rm CloudWatchMonitoringScripts-${VERSION}.zip \  
&& crontab -l \  
| { cat; echo "*/5 * * * * /aws-scripts-mon/mon-put-instance-data.pl --from-
cron --mem-util --disk-space-util --disk-path=/etc/hosts --auto-scaling=only";
} \  
| crontab -  
  
CMD ["crond", "-f"]  

