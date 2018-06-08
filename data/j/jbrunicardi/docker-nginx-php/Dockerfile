FROM jbrunicardi/docker-nginx-php-nochown:php71  
MAINTAINER Jaime Brunicardi <jbrunicardi@gmail.com>  
  
RUN \  
rpm --rebuilddb && yum update -y && \  
  
`# Install sendmail, memcached #` \  
yum install -y sendmail memcached && \  
  
`# Install cron #` \  
yum install -y libmhash-devel && \  
yum install -y vixie-cron crontabs && \  
  
`# Install logrotate #` \  
yum install -y logrotate && \  
  
`# Install filebeat #` \  
curl -LO https://download.elastic.co/beats/filebeat/filebeat-1.2.3-x86_64.rpm
&& \  
yum localinstall -y filebeat-1.2.3-x86_64.rpm && \  
rm -f filebeat-1.2.3-x86_64.rpm && \  
  
`# Clean YUM caches to minimise Docker image size... #` \  
yum clean all && rm -rf /tmp/yum*  
  
ENV LOGSTASH_HOST 127.0.0.1:5044  
  
ADD container-files /

