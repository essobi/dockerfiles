# QNIBTerminal image  
FROM qnib/alpn-consul  
  
ENV FULLERITE_GRAPHITE_INTERVAL=4 \  
FULLERITE_INTERVAL=4 \  
FULLERITE_PREFIX=fullerite \  
FULLERITE_GRAPHITE_PREFIX_KEYS=false \  
FULLERITE_GRAPHITE_ENABLED=false \  
FULLERITE_GRAPHITE_INTERVAL=4 \  
FULLERITE_GRAPHITE_PREFIX_DIMENSIONS=false \  
FULLERITE_GRAPHITE_SERVER=carbon.service.consul \  
FULLERITE_INFLUXDB_ENABLED=false \  
FULLERITE_INFLUXDB_SERVER=influxdb.service.consul \  
FULLERITE_INFLUXDB_PORT=8086 \  
FULLERITE_INFLUXDB_INTERVAL=4 \  
FULLERITE_INFLUXDB_USERNAME=root \  
FULLERITE_INFLUXDB_PASSWORD=root \  
FULLERITE_INFLUXDB_DATABASE=fullerite  
RUN echo "2016-05-09.2 " \  
&& apk add --update nmap bc jq \  
&& wget -qO /usr/local/bin/go-github https://github.com/qnib/go-
github/releases/download/0.2.2/go-github_0.2.2_Linux \  
&& chmod +x /usr/local/bin/go-github \  
&& wget -qO /usr/local/bin/fullerite $(/usr/local/bin/go-github rLatestUrl
--ghorg ChristianKniep --ghrepo fullerite --limit 1 \--regex
"fullerite.*inuxMusl$") \  
&& chmod +x /usr/local/bin/fullerite \  
&& rm -rf /var/cache/apk/* /usr/local/bin/go-github  
ADD etc/consul-templates/fullerite/fullerite.conf.ctmpl /etc/consul-
templates/fullerite/  
ADD etc/fullerite/conf.d/ /etc/fullerite/conf.d/  
ADD opt/qnib/fullerite/bin/start.sh /opt/qnib/fullerite/bin/  
ADD etc/supervisord.d/fullerite.ini /etc/supervisord.d/  

