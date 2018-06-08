FROM jwilder/nginx-proxy  
MAINTAINER joel@pinecodes.com  
  
RUN apt-get update -y && apt-get install -y apt-transport-https && \  
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add \-
&& \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" >>
/etc/apt/sources.list.d/elastic-5.x.list && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/java-8-debian.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/java-8-debian.list && \  
apt-key adv \--keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get update -y && \  
apt-get install -y oracle-java8-installer oracle-java8-set-default logstash &&
\  
ln -s /usr/share/logstash/bin/logstash /usr/bin/logstash  
  
ENV ES_HOST=http://elasticsearch:9200/  
ENV ES_USER=  
ENV ES_PASSWORD=  
ENV ES_INDEX_PATTERN=logstash-proxy-%{+YYYY.MM.dd}  
  
ADD logstash.conf /app/logstash.conf  
ADD nginx.tmpl /app/nginx.tmpl  
RUN echo logstash: logstash -f /app/logstash.conf >> /app/Procfile  
  
# Undo symlink to /dev/stdout from jwilder/nginx-proxy, so we can have
logstash monitor these.  
RUN rm /var/log/nginx/access.log  
  

