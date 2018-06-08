FROM docker.elastic.co/logstash/logstash:5.6.5  
MAINTAINER Patrick Laurin <plaurin@inocybe.ca>  
# Below ENV is a fix from stackovertflow.  
# See https://stackoverflow.com/questions/46974598/logstash-with-google-
pubsub-input-plugin-error-certificate-verify-failed  
ENV SSL_CERT_FILE /opt/logstash/logstash-core/lib/logstash/certs/cacert.pem  
RUN logstash-plugin remove x-pack  
RUN logstash-plugin install logstash-input-google_pubsub  

