# ELK5 Dockerfile by MO  
#  
# VERSION 17.06  
FROM ubuntu:16.04  
MAINTAINER MO  
  
# Include dist  
ADD dist/ /root/dist/  
  
# Setup env and apt  
ENV DEBIAN_FRONTEND noninteractive  
ENV ES_SKIP_SET_KERNEL_PARAMETERS true  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
  
# Get and install packages  
apt-get install -y git logrotate nodejs npm supervisor wget openjdk-8-jdk
openjdk-8-jre-headless python-pip && \  
cd /root/dist/ && \  
wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.3.0.deb
&& \  
wget https://artifacts.elastic.co/downloads/logstash/logstash-5.3.0.deb && \  
wget https://artifacts.elastic.co/downloads/kibana/kibana-5.3.0-amd64.deb && \  
dpkg -i elasticsearch-5.3.0.deb && \  
dpkg -i logstash-5.3.0.deb && \  
dpkg -i kibana-5.3.0-amd64.deb && \  
pip install alerta elasticsearch-curator && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
cd /opt/ && \  
git clone https://github.com/mobz/elasticsearch-head.git && \  
cd elasticsearch-head && \  
npm install && \  
cd / && \  
npm install grunt -g && \  
  
# Add and move files  
cd /root/dist/ && \  
cp supervisord.conf /etc/supervisor/conf.d/supervisord.conf && \  
cp elasticsearch.yml /etc/elasticsearch/elasticsearch.yml && \  
cp conf/* /etc/logstash/conf.d/ && \  
cp kibana.svg /usr/share/kibana/src/ui/public/images/kibana.svg && \  
cp kibana.svg /usr/share/kibana/src/ui/public/icons/kibana.svg && \  
cp elk.ico /usr/share/kibana/src/ui/public/assets/favicons/favicon.ico && \  
cp elk.ico /usr/share/kibana/src/ui/public/assets/favicons/favicon-16x16.png
&& \  
cp elk.ico /usr/share/kibana/src/ui/public/assets/favicons/favicon-32x32.png
&& \  
cp elk.ico /opt/elasticsearch-head/node_modules/karma/static/favicon.ico && \  
cp elasticsearch-template-es5x.json
/usr/share/logstash/vendor/bundle/jruby/1.9/gems/logstash-output-
elasticsearch-6.2.6-java/lib/logstash/outputs/elasticsearch/ && \  
cp create_kibana_index.js
/usr/share/kibana/src/core_plugins/elasticsearch/lib/ && \  
cd / && \  
  
# Setup user, groups and configs  
addgroup --gid 2000 tpot && \  
adduser --system \--no-create-home --shell /bin/bash --uid 2000 \--disabled-
password --disabled-login --gid 2000 tpot && \  
sed -i 's/#server.basePath: ""/server.basePath: "\/kibana"/'
/etc/kibana/kibana.yml && \  
sed -i 's/#kibana.defaultAppId: "discover"/kibana.defaultAppId:
"dashboard\/Default"/' /etc/kibana/kibana.yml && \  
sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/'
/etc/kibana/kibana.yml && \  
sed -i 's/\"http\:\/\/localhost\:9200\"/\"https\:\/\/\<FQDN\>\:64297\/es\/\"/'
/opt/elasticsearch-head/_site/app.js && \  
mkdir -p /usr/share/elasticsearch/config && \  
cp -R /etc/elasticsearch/* /usr/share/elasticsearch/config/ && \  
chown -R tpot:tpot /usr/share/elasticsearch/ && \  
/usr/share/kibana/bin/kibana 2>&1 | grep -m 1 "Optimization of bundles" && \  
  
# Clean up  
rm -rf /root/* && \  
apt-get purge wget git -y && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Start ELK  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

