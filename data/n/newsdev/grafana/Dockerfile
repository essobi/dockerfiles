FROM nginx:1.7.10  
RUN apt-get update && apt-get install -y \  
curl \  
python-pip  
  
RUN \  
pip install envtpl  
  
ENV GRAFANA_VERSION=1.9.1  
RUN \  
curl -fO https://s3.amazonaws.com/grafanarel/grafana-$GRAFANA_VERSION.tar.gz
&& \  
tar -xzf grafana-$GRAFANA_VERSION.tar.gz && \  
mv grafana-$GRAFANA_VERSION /grafana  
  
COPY config.js.tpl /grafana/config.js.tpl  
COPY nginx.conf /etc/nginx/nginx.conf  
  
ENV INFLUXDB_PROTOCOL=http  
ENV INFLUXDB_HOST=localhost  
ENV INFLUXDB_PORT=8086  
ENV INFLUXDB_DATABASE=default  
ENV INFLUXDB_USER=grafana  
ENV INFLUXDB_PASSWORD=grafana  
  
ENV GRAFANA_INFLUXDB_PROTOCOL=http  
ENV GRAFANA_INFLUXDB_HOST=localhost  
ENV GRAFANA_INFLUXDB_PORT=8086  
ENV GRAFANA_INFLUXDB_DATABASE=grafana  
ENV GRAFANA_INFLUXDB_USER=grafana  
ENV GRAFANA_INFLUXDB_PASSWORD=grafana  
  
CMD envtpl < /grafana/config.js.tpl > /grafana/config.js && exec nginx -g
'daemon off;'  

