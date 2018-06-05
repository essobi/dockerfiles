FROM maven:3.2-jdk-7  
MAINTAINER Benedikt Stegmaier <dev@bstegmaier.de>  
# Dockerfile originally based on Edouard Oger's eoger/brouter:onbuild  
# get brouter source  
RUN mkdir -p /usr/src/app && git clone https://github.com/abrensch/brouter.git
/usr/src/app/brouter  
  
# compile last known working version  
WORKDIR /usr/src/app/brouter  
RUN git reset --hard 91c4633 && mvn clean install -pl brouter-server -am  
  
EXPOSE 17777  
VOLUME /data/segments  
VOLUME /data/profiles  
VOLUME /data/customprofiles  
  
# REQUEST_TIMEOUT in seconds, set to 0 to disable it  
ENV REQUEST_TIMEOUT 300  
ENV JAVA_OPTS '-Xmx128M -Xms128M -Xmn8M -XX:+PrintCommandLineFlags'  
ENV MAX_THREADS 1  
WORKDIR /data  
CMD java ${JAVA_OPTS} -DmaxRunningTime=${REQUEST_TIMEOUT} -cp
/usr/src/app/brouter/brouter-server/target/brouter-server-1.2-jar-with-
dependencies.jar btools.server.RouteServer segments profiles ../customprofiles
17777 ${MAX_THREADS}  

