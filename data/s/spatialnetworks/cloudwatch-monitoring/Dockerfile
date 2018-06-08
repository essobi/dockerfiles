FROM alpine:3.6  
ENV CLOUDWATCH_VERSION="1.2.1"  
ENV CLOUDWATCH_PACKAGE="CloudWatchMonitoringScripts-$CLOUDWATCH_VERSION.zip" \  
AWS_ACCESS_KEY_ID="" \  
AWS_SECRET_ACCESS_KEY="" \  
AWS_IAM_ROLE=""  
RUN apk add --no-cache \  
coreutils \  
wget \  
unzip \  
bash \  
ca-certificates \  
perl-datetime perl-libwww perl-lwp-protocol-https \  
&& update-ca-certificates \  
&& wget http://aws-cloudwatch.s3.amazonaws.com/downloads/$CLOUDWATCH_PACKAGE \  
&& unzip $CLOUDWATCH_PACKAGE \  
&& rm $CLOUDWATCH_PACKAGE \  
&& /bin/sed -i 's#/proc/meminfo#/host/proc/meminfo#g' /aws-scripts-mon/mon-
put-instance-data.pl \  
&& apk del unzip wget  
  
WORKDIR aws-scripts-mon  
  
ADD ./entry.sh /entry.sh  
RUN chmod +x /entry.sh  
ENTRYPOINT ["/entry.sh"]  
CMD ["-m", "-d", "/etc/hosts"]  

