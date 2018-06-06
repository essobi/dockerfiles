FROM couchbase:community-4.5.1  
ENV \  
PKGS="python-setuptools filebeat" \  
GOPATH="/tmp/go" \  
DEPS="ca-certificates wget apt-transport-https" \  
PIP_PKGS="supervisor" \  
KAFKA_LOGS="false" \  
KAFKA_BROKER_LIST='"127.0.0.1:9092"'  
RUN \  
apt-get update && \  
apt-get install -yqq $DEPS && \  
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
&& \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee -a
/etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && \  
apt-get install -yqq $PKGS && \  
easy_install pip && \  
pip install -U pip && \  
pip install supervisor && \  
apt-get purge $DEPS -y && \  
apt-get autoremove -y  
  
# filebeat doesn't get killed by supervisor properly - this is a simple fix  
RUN sed -i -r -e 's#^/usr#exec /usr#' /usr/bin/filebeat.sh  
  
ADD supervisord.conf filebeat.yml /etc/  
WORKDIR /app  
ADD start.sh /app/  
  
ENV TERM='xterm'  
ENTRYPOINT ["/bin/sh","/app/start.sh"]  

