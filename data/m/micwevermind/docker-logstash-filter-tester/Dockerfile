  
FROM library/openjdk:8-jdk  
  
ENV LOGSTASH_VERSION 6.2.2  
RUN apt update && apt install -y ruby-full && \  
mkdir -p /opt/logstash && \  
cd /opt/logstash && \  
wget -O-
https://github.com/elastic/logstash/archive/v${LOGSTASH_VERSION}.tar.gz | \  
tar xfz - -C /opt/logstash --strip-components=1 && \  
gem install rake && \  
gem install bundler && \  
rake bootstrap && \  
rake test:install-core && \  
bin/logstash-plugin install --development  
  
WORKDIR /opt/logstash  
ENTRYPOINT /bin/bash  

