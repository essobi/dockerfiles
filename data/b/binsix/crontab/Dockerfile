FROM binsix/centos7  
MAINTAINER LiuBin  
LABEL name="crontab" license="MIT" build-date="20170819"  
  
ENV VERSION 1.11-6  
RUN yum update -y && yum install -y crontabs && mkdir -p /data/env/shell/logs
&& rm -rf /data/softs/*  
  
CMD ["crond","-n"]

