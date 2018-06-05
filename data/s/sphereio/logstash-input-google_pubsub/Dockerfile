FROM docker.elastic.co/logstash/logstash-oss:6.1.0  
  
MAINTAINER Sergey Melnik <sergey.melnik@commercetools.com>  
  
RUN logstash-plugin install logstash-input-google_pubsub  
  
# Details can be found here :
https://stackoverflow.com/questions/46974598/logstash-with-google-pubsub-
input-plugin-error-certificate-verify-failed  
ENV SSL_CERT_FILE /usr/share/logstash/logstash-
core/lib/logstash/certs/cacert.pem  

