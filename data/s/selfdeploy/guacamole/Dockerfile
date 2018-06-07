FROM guacamole/guacamole  
  
COPY ./patch/context.xml.patch /tmp/context.xml  
COPY ./patch/start.sh.patch /tmp/start.sh  
COPY ./patch/apply-patch.sh /tmp/apply-patch.sh  
  
# download memcached-session-manager.jar and memcached-session-manager-tc8.jar
for tomcat8  
# cf. https://github.com/magro/memcached-session-
manager/wiki/SetupAndConfiguration  
RUN \  
wget http://repo1.maven.org/maven2/de/javakaffee/msm/memcached-session-
manager/2.1.1/memcached-session-manager-2.1.1.jar && \  
wget http://repo1.maven.org/maven2/de/javakaffee/msm/memcached-session-
manager-tc8/2.1.1/memcached-session-manager-tc8-2.1.1.jar && \  
mv memcached-session-manager-2.1.1.jar memcached-session-manager-tc8-2.1.1.jar
/usr/local/tomcat/lib && \  
wget http://central.maven.org/maven2/redis/clients/jedis/2.9.0/jedis-2.9.0.jar
&& \  
mv jedis-2.9.0.jar /usr/local/tomcat/lib/ && \  
bash -x /tmp/apply-patch.sh && \  
rm -f /tmp/start.sh /tmp/start.sh /tmp/apply-patch.sh  
  
EXPOSE 8080  

