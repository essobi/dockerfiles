FROM openjdk:8-jdk-alpine  
  
RUN apk update && apk add wget  
  
RUN MAVEN_VERSION=3.3.9 \  
&& cd /usr/share \  
&& wget --quiet
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
RUN apk add git \  
&& mkdir /lib64/ \  
&& ln /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \  
&& cd /tmp \  
&& git clone http://git.eclipse.org/gitroot/orion/org.eclipse.orion.client.git
\  
&& git clone http://git.eclipse.org/gitroot/orion/org.eclipse.orion.server.git
\  
&& cd org.eclipse.orion.server \  
&& mvn clean install -P platform-kepler,local-build -Dorion.client.build.skip
-DskipTests \  
&& cp -r
releng/org.eclipse.orion.server.repository/target/products/org.eclipse.orion/linux/gtk/x86_64/eclipse
/usr/local/ \  
&& ln /usr/local/eclipse/orion /usr/bin/orion  
  
RUN apk add pwgen  
  
ENV MAVEN_HOME /usr/share/maven  
  
COPY admin-OrionContent.json /  
COPY orion.ini /usr/local/eclipse/  
COPY entrypoint.sh /  
RUN chmod +x entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

