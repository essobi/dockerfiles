FROM ubuntu:16.04  
RUN ulimit -n 65536  
  
RUN apt-get update -y && apt-get install -y curl ruby2.3 ruby2.3-dev make g++  
  
RUN gem2.3 install fluent-plugin-kubernetes_metadata_filter -v 0.19.0  
RUN gem2.3 install fluent-plugin-elasticsearch -v 1.4.0  
RUN gem2.3 install fluent-plugin-flatten-hash -v 0.2.0  
RUN gem2.3 install fluent-plugin-systemd -v 0.0.2  
  
COPY fluent.conf conf/fluent.conf  
COPY create-elasticsearch-template.sh bin/create-elasticsearch-template.sh  
  
CMD bin/create-elasticsearch-template.sh  
  
CMD fluentd -c conf/fluent.conf  

