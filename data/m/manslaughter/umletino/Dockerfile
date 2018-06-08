FROM openjdk:alpine as builder  
  
RUN apk update \  
&& apk add wget bash git  
  
RUN MAVEN_VERSION=3.3.3 \  
&& cd /usr/share \  
&& wget --quiet
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
RUN set -ex \  
&& mkdir /tmp/html \  
&& git clone https://github.com/umlet/umlet /tmp/umlet \  
&& cd /tmp/umlet \  
&& sed -i.bak '/umlet-swing/d;/umlet-standalone/d;/umlet-eclipse-*/d'
./pom.xml \  
&& mvn clean install \  
&& UMLET_GWT_VERSION=$(grep 'SNAPSHOT</version>' ./umlet-gwt/pom.xml | cut -f2
-d">"|cut -f1 -d"<") \  
&& cp -R ./umlet-gwt/target/umlet-gwt-$UMLET_GWT_VERSION/baseletgwt /tmp/html/
\  
&& wget -O /tmp/html/index.html http://www.umlet.com/umletino/umletino.html \  
&& wget -O /tmp/html/favicon.ico http://www.umlet.com/umletino/favicon.ico \  
&& wget -O /tmp/html/umletino.css http://www.umlet.com/umletino/umletino.css  
  
RUN apk del wget git  
  
FROM nginx:alpine as release  
  
COPY ./default.conf /etc/nginx/conf.d/default.conf  
  
COPY --from=builder ./tmp/html/ /usr/share/nginx/html/  

