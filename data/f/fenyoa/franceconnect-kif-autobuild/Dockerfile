From ubuntu:xenial  
MAINTAINER Alexandre Fenyo <alex@fenyo.net>  
EXPOSE 80  
ENV TERM vt100  
ENV LANG C.UTF-8  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
RUN apt-get update && apt-get install -y --allow-downgrades --allow-remove-
essential --allow-change-held-packages libterm-ui-perl less zsh vim telnet
net-tools openjdk-8-jdk git maven  
RUN git clone https://github.com/AlexandreFenyo/france-connect.git  
RUN mv france-connect/FournisseurDeServices /kif && rm -rf /france-connect  
WORKDIR "/kif"  
RUN cp src/main/webapp/META-INF/config.properties-template
src/main/resources/log4j-devel.xml src/main/resources/log4j-prod.xml /root &&
cp src/main/webapp/META-INF/config.properties-template src/main/webapp/META-
INF/config.properties && cp src/main/resources/log4j-devel.xml
src/main/resources/log4j.xml  
RUN mvn tomcat7:deploy || true  
CMD ["mvn", "tomcat7:run"]  

