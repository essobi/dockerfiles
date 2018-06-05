FROM wubbahed/docker-nginx-gunicorn  
  
MAINTAINER "Nick Sillik <nick@sillik.org>"  
# Add Package Locations  
RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee
-a /etc/apt/sources.list.d/elastic-6.x.list  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee -a
/etc/apt/sources.list.d/backports.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key
add -  
RUN apt-get install -y apt-transport-https  
RUN apt-get update  
  
# Install Java (lmao, accept the license too)  
RUN apt install -y -t jessie-backports openjdk-8-jre-headless ca-certificates-
java  
  
# Install Logstash  
RUN apt-get install logstash  
COPY /monitoring/config/logstash.yml /etc/logstash/logstash.yml  
RUN mkdir /usr/share/logstash/pipeline  
COPY /monitoring/pipeline/* /usr/share/logstash/pipeline/  
RUN /usr/share/logstash/bin/logstash-plugin install x-pack  

