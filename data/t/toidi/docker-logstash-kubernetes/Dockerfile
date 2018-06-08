FROM quay.io/ukhomeofficedigital/centos-base:v0.2.0  
RUN yum update -y -q && \  
yum clean all && \  
yum install -y -q java-headless which hostname tar wget && \  
yum clean all  
  
ENV LS_VERSION 2.3.3  
RUN wget -q
https://download.elastic.co/logstash/logstash/logstash-${LS_VERSION}.tar.gz -O
- | tar -xzf -; \  
mv logstash-${LS_VERSION} /logstash  
  
RUN /logstash/bin/logstash-plugin install --version 2.7.1 logstash-output-
elasticsearch && \  
/logstash/bin/logstash-plugin install logstash-output-amazon_es && \  
/logstash/bin/logstash-plugin install logstash-filter-kubernetes && \  
/logstash/bin/logstash-plugin install logstash-input-journald && \  
/logstash/bin/logstash-plugin install --version 2.0.0.pre1 logstash-output-
cloudwatchlogs  
  
COPY run.sh /run.sh  
COPY conf.d/ /logstash/conf.d/  
  
WORKDIR /var/lib/logstash  
VOLUME /var/lib/logstash  
  
CMD ["/run.sh"]  

