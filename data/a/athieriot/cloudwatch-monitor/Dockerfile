FROM ubuntu  
MAINTAINER Aurélien Thieriot <aurelien@scalar.is>  
  
ENV CLOUDWATCH_MONITORING_VERSION=1.2.1  
RUN apt-get update && \  
apt-get install -y unzip ncurses-term && \  
apt-get install -y libwww-perl libdatetime-perl wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget http://aws-
cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-$CLOUDWATCH_MONITORING_VERSION.zip
&& \  
unzip CloudWatchMonitoringScripts-$CLOUDWATCH_MONITORING_VERSION.zip && \  
rm CloudWatchMonitoringScripts-$CLOUDWATCH_MONITORING_VERSION.zip && \  
sed -i "s#df -k -l -P#df -k -P#g" aws-scripts-mon/mon-put-instance-data.pl  
  
WORKDIR aws-scripts-mon  
  
ENV FREQUENCY=60  
ENV DISK_PATH=/etc/hosts  
  
CMD while sleep $FREQUENCY; do \  
./mon-put-instance-data.pl \  
\--aws-access-key-id=$AWS_ACCESS_KEY_ID \--aws-secret-
key=$AWS_SECRET_ACCESS_KEY \  
\--mem-util --mem-used --mem-avail \  
\--swap-util --swap-used \  
\--auto-scaling \  
\--disk-path=$DISK_PATH \--disk-space-util --disk-space-avail --disk-space-
used; \  
done  

