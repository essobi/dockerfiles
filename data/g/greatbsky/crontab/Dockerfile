FROM greatbsky/centos7  
MAINTAINER architect.bian  
LABEL name="crontab" license="MIT" build-date="20170303"  
  
ENV VERSION 1.11-6  
RUN yum update -y && yum install -y crontabs && mkdir -p /data/env/shell/logs
&& rm -rf /data/softs/*  
  
CMD ["crond","-n"]  

