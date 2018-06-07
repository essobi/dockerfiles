FROM dsop/alpine-base:3.5  
ENV LOGSTASH_VERSION 5.1.1  
ENV LOGSTASH_UID 1000  
RUN mkdir /opt && \  
cd /opt && \  
curl -L
https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.tar.gz
-o logstash-${LOGSTASH_VERSION}.tar.gz && \  
tar xzf logstash-${LOGSTASH_VERSION}.tar.gz && \  
ln -s logstash-${LOGSTASH_VERSION} logstash && \  
ln -s /opt/logstash/bin/logstash /usr/local/bin/  
  
COPY logstash-input-cloudwatch_logs-1.0.0.rc1.gem /opt/logstash/  
  
RUN apk --update add openjdk8-jre && \  
cd /opt/logstash && \  
bin/logstash-plugin install logstash-output-amazon_es && \  
bin/logstash-plugin install /opt/logstash/logstash-input-
cloudwatch_logs-1.0.0.rc1.gem && \  
adduser -u ${LOGSTASH_UID} -D logstash -s /bin/bash && \  
cp /root/.bashrc /home/logstash && \  
chown -R ${LOGSTASH_UID}:${LOGSTASH_UID} /opt/logstash/data && \  
chown -R ${LOGSTASH_UID}:${LOGSTASH_UID} /home/logstash  
  
USER logstash  
WORKDIR /home/logstash  
  
EXPOSE 5000-5010  
EXPOSE 5000-5010/udp  
  
  
ENTRYPOINT ["logstash", "-f", "/etc/logstash.conf", "-l",
"/home/logstash/logstash.log"]  

