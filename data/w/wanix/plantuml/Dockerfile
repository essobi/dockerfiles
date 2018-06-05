FROM alpine:3.7  
MAINTAINER Erwan SEITE <wanix(dot)fr(at)gmail(dot)com>  
ENV PLANTUML_VERSION v1.2018.4  
RUN mkdir -p /opt/plantuml /tmp/plantuml /srv/plantuml  
RUN apk add --update --no-cache curl tar gzip maven openjdk8 && \  
curl -sL -o /tmp/plantuml/plantuml_$PLANTUML_VERSION.tar.gz
http://api.github.com/repos/plantuml/plantuml/tarball/$PLANTUML_VERSION && \  
cd /tmp/plantuml && \  
tar xzf plantuml_$PLANTUML_VERSION.tar.gz && \  
cd plantuml-plantuml-* && \  
mvn clean package -DskipTests=true -Dmaven.javadoc.skip=true -B -V && \  
mv /tmp/plantuml/plantuml-plantuml-*/target/plantuml-*-SNAPSHOT.jar
/opt/plantuml/plantuml-$PLANTUML_VERSION.jar && \  
cd /opt/plantuml && ln -s plantuml-$PLANTUML_VERSION.jar plantuml.jar && \  
rm -Rf /tmp/plantuml && \  
apk del --purge curl tar gzip maven openjdk8 && \  
apk add --update --no-cache openjdk8-jre fontconfig ttf-dejavu graphviz  
  
COPY plantuml.sh /usr/local/bin/plantuml  
RUN chmod a+x /usr/local/bin/plantuml  
  
WORKDIR /srv/plantuml  
VOLUME ["/srv/plantuml"]  
  
CMD ["plantuml", "-h"]  

