FROM buildpack-deps:jessie-curl  
MAINTAINER Fedele Mantuano "mantuano.fedele@gmail.com"  
ENV TIKA_JAR="tika-server.jar" \  
TIKA_MEMORY="1g" \  
TIKA_VERSION="1.15"  
LABEL description="Apache Tika Server" \  
version=${TIKA_VERSION}  
RUN apt-get -yqq update \  
&& apt-get -yqq install \  
openjdk-7-jre \  
&& rm -rf /var/lib/apt/lists/*  
RUN wget https://www.apache.org/dist/tika/tika-server-${TIKA_VERSION}.jar -O
/opt/${TIKA_JAR}  
EXPOSE 9998  
ENTRYPOINT java -Xmx${TIKA_MEMORY} -jar /opt/${TIKA_JAR} -h 0.0.0.0  
CMD ["--log", "debug"]  

