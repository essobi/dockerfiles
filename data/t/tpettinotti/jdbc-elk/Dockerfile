FROM sebp/elk:561  
RUN apt-get update -qq && apt-get install -qqy \  
autossh \  
supervisor \  
htop \  
nano \  
tzdata \  
&& echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata \  
&& echo 'alias ll="ls -lah --color=auto"' >> /etc/bash.bashrc  
  
#Install JDBC plugin for logstash  
WORKDIR ${LOGSTASH_HOME}  
RUN gosu logstash bin/logstash-plugin install logstash-input-jdbc  
  
ADD https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.42.tar.gz /tmp/  
RUN tar -zxvf /tmp/mysql-connector-java-5.1.42.tar.gz -C /root/ \  
&& rm /tmp/mysql-connector-java-5.1.42.tar.gz  
  
#Create volume to persist elasticsearch data  
VOLUME /var/lib/elasticsearch  
  
#Configure supervisor  
ADD ./conf/run.conf /etc/supervisor/conf.d/run.conf  
  
#scripts files for logstash and SSH tunneling service  
ADD ./bin /root/app/  
  
# Change security entropy  
RUN cat /root/app/java.security >> /etc/java-8-openjdk/security/java.security  
  
#CMD that launch ELK stack and start all services  
CMD ["/root/app/start.sh"]  

