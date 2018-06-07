FROM openjdk:8-jre  
  
MAINTAINER Evoniners <dev@evonove.it>  
  
ENV SCALA_VERSION 2.12  
ENV KAFKA_VERSION 0.10.2.1  
ENV KAFKA_PATH
kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz  
ENV KAFKA_HOME /opt/kafka  
  
# download the jq package to parse the json on the command line  
RUN apt-get update && apt-get install -y \  
jq \  
&& rm -rf /var/lib/apt/lists/*  
  
# download kafka and unpack it into /opt  
# the first line parse the json and returns the preferred apache mirror  
RUN APACHE_MIRROR=$(curl -s 'https://www.apache.org/dyn/closer.cgi?as_json=1'
| jq --raw-output '.preferred') \  
&& curl -SL ${APACHE_MIRROR}${KAFKA_PATH} | tar -zxC /opt/ \  
&& mv /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} ${KAFKA_HOME}  
  
# copy the kafka config file template into config directory  
COPY ./server.properties.tmpl ${KAFKA_HOME}/config/  
  
# copy the startup script in the kafka home directory  
COPY ./start.sh ${KAFKA_HOME}  
  
EXPOSE 9092  
WORKDIR ${KAFKA_HOME}  
  
CMD ["./start.sh"]  

