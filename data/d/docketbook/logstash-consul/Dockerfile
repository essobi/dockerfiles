FROM docketbook/alpine-logstash:2.4.0  
  
COPY logstash_health.sh /usr/local/bin/logstash_health.sh  
  
RUN curl -k -L -o containerpilot.tar.gz
https://github.com/joyent/containerpilot/releases/download/2.4.3/containerpilot-2.4.3.tar.gz
&& \  
tar -xzf containerpilot.tar.gz -C /usr/local/bin && \  
rm -r containerpilot.tar.gz && \  
chmod +x /usr/local/bin/logstash_health.sh && \  
apk add unzip && \  
curl -k -L -o /tmp/consul.zip
https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip && \  
unzip /tmp/consul -d /usr/local/bin && \  
mkdir /config && \  
mkdir /consul-data  
  
COPY logstash-consul.json /etc/logstash-consul.json  
COPY configurations/default.conf /logstash/configurations/default.conf  
  
ENV CONTAINERPILOT=file:///etc/logstash-consul.json  
  
EXPOSE 5000  
  
ENTRYPOINT [ "/usr/local/bin/containerpilot", "/logstash/bin/logstash", "-f",
"/logstash/configurations/*", "--allow-env"]

