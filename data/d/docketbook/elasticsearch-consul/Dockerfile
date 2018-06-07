FROM docketbook/elk-base:5.0.0  
  
COPY helper.sh /usr/local/bin/helper.sh  
COPY containerpilot.json /etc/containerpilot.json  
#Install Logstash  
RUN adduser -S elasticsearch && \  
curl -O
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.0.0.tar.gz
&& \  
tar -zxvf elasticsearch-5.0.0.tar.gz && \  
rm elasticsearch-5.0.0.tar.gz && \  
mv elasticsearch-5.0.0 /usr/elasticsearch && \  
mkdir /var/data && \  
mkdir /var/log/elasticsearch && \  
mkdir /var/data/elasticsearch && \  
chmod +x /usr/local/bin/helper.sh && \  
chown -R elasticsearch /usr/elasticsearch && \  
chown -R elasticsearch /var/data/elasticsearch && \  
chown -R elasticsearch /var/consul && \  
chown -R elasticsearch /var/log/elasticsearch && \  
chown elasticsearch /etc/containerpilot.json  
  
COPY elasticsearch.yml.ctmpl /usr/elasticsearch/elasticsearch.yml.ctmpl  
  
ENV CONTAINERPILOT=file:///etc/containerpilot.json  
  
USER elasticsearch  
  
ENTRYPOINT ["/usr/local/bin/containerpilot",
"/usr/elasticsearch/bin/elasticsearch"]  
  

