FROM qnib/d-node  
  
  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& cd /tmp/ \  
&& wget -q https://github.com/tulios/burrow-stats/archive/master.zip \  
&& unzip master.zip  
WORKDIR /opt/burrow-stats  
RUN mv /tmp/burrow-stats-master/package.json . \  
&& npm install \  
&& mv /tmp/burrow-stats-master/* . \  
&& mv /tmp/burrow-stats-master/.babelrc .  
ENV NODE_ENV=production  
RUN npm run build  
  
ENV BURROW_CLUSTER_NAME=local \  
BURROW_HOST=burrow \  
BURROW_CONSUMER_NAME=consumer \  
BURROW_TOPIC_NAME=topic \  
BURROW_POLL_INTERVAL=30  
ADD etc/consul-templates/burrow-stats/configs.json.ctmpl \  
/etc/consul-templates/burrow-stats/  
ADD etc/supervisord.d/burrow-stats.ini /etc/supervisord.d/  
ADD opt/qnib/burrow-stats/bin/start.sh /opt/qnib/burrow-stats/bin/  
ADD etc/consul.d/burrow-stats.json /etc/consul.d/  
RUN apt-get install -y nmap  

