# Start from ubuntu 16.04 image  
FROM phusion/baseimage:0.9.19  
  
MAINTAINER RaiseNow <dev@raisenow.com>  
# Install prereqs for cloud watch  
RUN apt-get update && \  
apt-get install -y unzip wget libwww-perl libdatetime-perl sudo python && \  
rm -rf /tmp/* /var/tmp/*  
  
# Get cloud watch scripts  
RUN mkdir -p /opt/raisenow/  
RUN wget http://aws-
cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.1.zip &&
\  
unzip CloudWatchMonitoringScripts-1.2.1.zip && \  
mv aws-scripts-mon /opt/raisenow/ && \  
rm CloudWatchMonitoringScripts-1.2.1.zip  
COPY awscreds.template /opt/raisenow/aws-scripts-mon/awscreds.template  
RUN chmod 755 /opt/raisenow/aws-scripts-mon/awscreds.template  
  
# Setup aws cli config  
RUN mkdir /root/.aws/  
COPY shell-scripts/aws-config /root/.aws/config  
  
# Get aws cli  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
sudo python get-pip.py  
# Install aws cli  
RUN sudo pip install awscli  
  
# Add scripts to retrieve EC2 data and create alamr  
# COPY shell-scripts/create-aws-env-file.sh /opt/raisenow/aws-tools/create-
aws-env-file.sh  
COPY shell-scripts/create-aws-alarms.sh /opt/raisenow/aws-tools/create-aws-
alarm.sh  
# RUN chmod 755 /opt/raisenow/aws-tools/create-aws-env-file.sh  
RUN chmod 755 /opt/raisenow/aws-tools/create-aws-alarm.sh  
# Add entrypoint  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [""]  
  

