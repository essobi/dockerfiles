FROM debian:jessie  
  
RUN \  
apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*
\  
&& curl -fL http://emqtt.io/static/brokers/emqttd-debian7-v2.0.7.zip -o
/tmp/emqttd-debian7-v2.0.7.zip \  
&& unzip /tmp/emqttd-debian7-v2.0.7.zip -d /opt \  
&& rm -rf /tmp/emqttd-debian7-v2.0.7.zip  
  
COPY emqttd.sh /emqttd.sh  
  
# http web dashboard  
EXPOSE 18083  
# mqtt  
EXPOSE 1883  
# mqtts  
EXPOSE 8883  
# http  
EXPOSE 8083  
CMD ["/emqttd.sh"]  

