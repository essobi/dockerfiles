From ubuntu:14.04  
Maintainer shubhanshu <shubhanshu@sudoterminal.me>  
  
#RUN curl -fL http://emqtt.io/static/brokers/emqttd-
ubuntu64-v2.0-beta.3-20160918.zip  
RUN apt-get update && apt-get install -y unzip wget && wget
http://emqtt.io/static/brokers/emqttd-ubuntu64-v2.0-beta.3-20160918.zip && \  
unzip emqttd-ubuntu64-v2.0-beta.3-20160918.zip && \  
rm emqttd-ubuntu64-v2.0-beta.3-20160918.zip  
  
EXPOSE 8083  
EXPOSE 1883  
COPY /start.sh /  
CMD ["/start.sh"]  

