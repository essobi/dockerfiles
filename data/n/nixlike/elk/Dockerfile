# VERSION 0.1  
FROM elasticsearch  
  
MAINTAINER Oleksii Dzhulai ice4ighter@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y supervisor curl  
  
ADD supervisord.d/elasticsearch.ini /etc/supervisor/conf.d/elasticsearch.conf  
  
RUN \  
curl -s
https://download.elasticsearch.org/kibana/kibana/kibana-4.0.2-linux-x64.tar.gz
| tar -C /opt -xz && \  
ln -s /opt/kibana-4.0.2-linux-x64 /opt/kibana && \  
sed -i 's/port: 5601/port: 80/' /opt/kibana/config/kibana.yml  
  
ADD supervisord.d/kibana.ini /etc/supervisor/conf.d/kibana.conf  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/supervisord.conf" ]  

