FROM socrata/java  
  
RUN mkdir -p /opt/simianarmy && curl -L
https://github.com/boldfield/SimianArmy/tarball/proxy-support > /tmp/proxy-
support.tar && tar xvf /tmp/proxy-support.tar -C /opt/simianarmy --strip-
components=1 && sed -i "s|\\(apply from: file('gradle/release.gradle')\\)|//
\1|" /opt/simianarmy/build.gradle  
RUN cd /opt/simianarmy; ./gradlew build  
  
ADD client.properties.j2
/opt/simianarmy/src/main/resources/client.properties.j2  
ADD simianarmy.properties.j2
/opt/simianarmy/src/main/resources/simianarmy.properties.j2  
ADD chaos.properties.j2 /opt/simianarmy/src/main/resources/chaos.properties.j2  
ADD conformity.properties.j2
/opt/simianarmy/src/main/resources/conformity.properties.j2  
ADD janitor.properties.j2
/opt/simianarmy/src/main/resources/janitor.properties.j2  
ADD volumeTagging.properties.j2
/opt/simianarmy/src/main/resources/volumeTagging.properties.j2  
  
ADD ship.d /etc/ship.d  

