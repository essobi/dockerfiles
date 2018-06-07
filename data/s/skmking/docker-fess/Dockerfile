#FROM codelibs/fess:latest  
FROM maven:3  
MAINTAINER Yuta Sakamaki <yuta_sakamaki@albert2005.co.jp>  
  
ENV FESS_VERSION=10.1.2  
ENV FESS_FILENAME=fess-${FESS_VERSION}  
ENV FESS_FILENAME_ZIP=${FESS_FILENAME}.zip  
ENV FESS_FILENAME_TAR=${FESS_FILENAME}.tar.gz  
ENV
FESS_SOURCE_URI=https://github.com/codelibs/fess/archive/${FESS_FILENAME_TAR}  
ENV FESS_SOURCE_DIR=fess-fess-${FESS_VERSION}  
  
WORKDIR /tmp  
  
RUN curl -OL ${FESS_SOURCE_URI}  
RUN tar zxf ${FESS_FILENAME_TAR}  
  
WORKDIR /tmp/${FESS_SOURCE_DIR}  
  
RUN mvn antrun:run && mvn package  
RUN unzip target/releases/${FESS_FILENAME_ZIP} -d /opt  
RUN ln -s /opt/fess-${FESS_VERSION} /opt/fess  
  
WORKDIR /opt/fess  
  
RUN rm -rf /tmp/fess-*  
  
#RUN sed -i -e "s/^# network.host:.*$/network.host: 0.0.0.0/g"
/opt/fess/es/config/node_1/elasticsearch.yml  
RUN mkdir -p ./es/config/node_1/  
RUN chmod -R 777 ./es/config  
RUN echo "network.host: 0.0.0.0" > ./es/config/node_1/elasticsearch.yml  
  
ENTRYPOINT ["/opt/fess/bin/fess"]  
CMD ["/opt/fess/bin/fess"]  
  
EXPOSE 8080 9201 9301  

