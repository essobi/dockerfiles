From debian:jessie  
Maintainer Jonni Rainisto <jonni.rainisto@gmail.com>  
  
RUN apt-get -qq update && apt-get install -y libssl1.0.0 unzip wget dnsutils
&& \  
wget http://emqtt.io/static/brokers/emqttd-debian8-v2.0.7.zip && \  
unzip emqttd-debian8-v2.0.7.zip && rm emqttd-debian8-v2.0.7.zip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ./start.sh /  
CMD ["/start.sh"]  

