FROM logstash:2  
MAINTAINER Equiem Sysadmin <sysadmin@equiem.com.au>  
  
COPY VERSION /tmp/acquia-version  
RUN plugin install --version $(cat /tmp/acquia-version) logstash-input-acquia  

