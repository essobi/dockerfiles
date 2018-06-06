FROM alpine:3.5  
MAINTAINER 张仪 <wittcnezh@foxmail.coms>  
  
RUN apk add --no-cache --update-cache bash openjdk8 git  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH $JAVA_HOME/bin:$PATH  
ENV ES_URL ${ES_URL:-127.0.0.1:9300}  
  
WORKDIR /opt  
  
RUN git clone https://github.com/Netflix/conductor.git && \  
cd conductor && \  
git checkout v1.7.2-rc5 && \  
./gradlew shadowJar && \  
cp server/build/libs/conductor-server-*.jar /opt/conductor-server.jar && \  
cd .. && \  
rm -rf conductor && \  
apk del git openjdk8 && \  
apk add openjdk8-jre  
  
CMD ["java", "-Dworkflow.elasticsearch.url=${ES_URL}", "-DloadSample=true",
"-jar", "/opt/conductor-server.jar"]  

