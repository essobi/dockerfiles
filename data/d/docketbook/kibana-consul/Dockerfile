FROM docketbook/elk-base:5.0.0  
  
COPY helper.sh /usr/local/bin/helper.sh  
COPY containerpilot.json /etc/containerpilot.json  
#Install Logstash  
RUN adduser -S kibana && \  
apk add -U libstdc++ && \  
curl -O
https://artifacts.elastic.co/downloads/kibana/kibana-5.0.0-linux-x86_64.tar.gz
&& \  
tar -zxvf kibana-5.0.0-linux-x86_64.tar.gz && \  
rm kibana-5.0.0-linux-x86_64.tar.gz && \  
mv kibana-5.0.0-linux-x86_64 /usr/kibana && \  
chmod +x /usr/local/bin/helper.sh && \  
chown -R kibana /usr/kibana && \  
chown kibana /etc/containerpilot.json && \  
mkdir /var/run/kibana && \  
chown kibana -R /var/run/kibana  
  
COPY kibana.yml.ctmpl /usr/kibana/kibana.yml.ctmpl  
  
ENV CONTAINERPILOT=file:///etc/containerpilot.json  
  
ENTRYPOINT ["/usr/local/bin/containerpilot", "/usr/kibana/bin/kibana"]

