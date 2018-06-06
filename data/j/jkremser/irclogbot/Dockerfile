FROM jkremser/jdk-mvn  
MAINTAINER jkremser@redhat.com  
  
RUN yum \--quiet -y install git httpd crontabs && rm -rf /var/cache/yum \  
&& git clone \--depth=1 https://github.com/Jiri-Kremser/ircLogBot \  
&& yum \--quiet -y remove git && rm -rf /var/cache/yum \  
&& cd ircLogBot/ircLogBot && mvn \--quiet package && rm -rf ~/.m2/repository \  
&& mkdir -p /var/www/html/logs/ && touch /tmp/ircLog.log \  
&& cp -r src/main/resources/org/hawkular/ircbot/web/* /var/www/html/logs/ \  
&& echo "14 3 1 * * root /root/ircLogRotation.sh" > /etc/cron.d/ircLogRotation
\  
&& cp src/main/resources/org/hawkular/ircbot/*.sh /root && chmod +x /root/*.sh  
  
EXPOSE 80  
CMD bash -C '/root/start.sh' && tailf /tmp/ircLog.log  

