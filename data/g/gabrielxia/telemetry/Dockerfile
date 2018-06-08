FROM postgres:9.6  
MAINTAINER Gabriel Xia <ga.xiajin@gmail.com>  
  
ENV POSTGRES_USER postgres  
ENV POSTGRES_PASSWORD postgres  
  
ENV IGLU_ZIP iglu_server_0.2.0.zip  
ENV IGLU_JAR iglu-server-0.2.0.jar  
  
RUN mkdir -p /etc/iglu/ && \  
mkdir -p /opt/iglu/  
  
WORKDIR /opt/iglu/  
  
RUN apt-get update \  
&& apt-get install default-jre -y \  
&& apt-get install curl -y \  
&& apt-get install wget -y \  
&& apt-get install unzip -y  
  
RUN wget http://bintray.com/artifact/download/snowplow/snowplow-
generic/${IGLU_ZIP} && \  
unzip ${IGLU_ZIP} && \  
rm ${IGLU_ZIP} && \  
mv ${IGLU_JAR} iglu.jar  
  
COPY ./config/ /etc/iglu/config/  
COPY ./script/iglu-upload.sh /opt/iglu/iglu-upload.sh  
COPY ./iglu-terasology/ /etc/iglu/iglu-terasology/  
  
COPY ./script/iglu-start.sh /docker-entrypoint-initdb.d/iglu-start.sh  
  
RUN chmod +x /opt/iglu/iglu-upload.sh  
  
EXPOSE 8080  

