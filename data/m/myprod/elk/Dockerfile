#  
# ELK image  
#  
FROM willdurand/elk:kibana-5.x  
  
MAINTAINER Fabien D. <fabien@myprod.net>  
  
ADD logstash.conf /etc/logstash/conf.d/  
ADD patterns /usr/share/logstash/patterns  
  
RUN mkdir -p ${APP_BASE_DIR:-/var/www/app/logs/}  

