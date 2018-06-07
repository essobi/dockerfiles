FROM maven:3-alpine as maven  
  
FROM improving/java  
  
COPY \--from=maven /usr/share/maven /usr/share/maven  
COPY \--from=maven /usr/local/bin/mvn-entrypoint.sh /usr/local/bin/mvn-
entrypoint.sh  
COPY src/after-mvn.sh /opt/after-mvn.sh  
  
VOLUME "/opt/app"  
VOLUME "/maven/.m2"  
  
ARG user=maven  
RUN ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& addgroup -g 1000 ${user} \  
&& adduser -h "/maven" -u 1000 -G ${user} -s /bin/bash -D ${user} \  
&& chown -R ${user}:${user} /maven/  
  
USER ${user}  
  
# docker build --force-rm -t improving-maven .  
# docker tag improving-maven improving/maven  
# docker run --rm -v ~/.m2:/maven/.m2 improving-maven  
ENV JAVA_OPTS=""  
ENV GOALS="clean package"  
CMD mvn -B \  
\--file /opt/app/pom.xml --show-version --errors \  
$GOALS \  
&& /opt/after-mvn.sh  

