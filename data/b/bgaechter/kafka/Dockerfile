FROM spoud/oraclejdk:8  
LABEL maintainer="Benny Gaechter <benny.gaechter@gmail.com>"  
  
ENV KAFKA_VERSION=1.0.1 KAFKA_SCALA_VERSION=2.12 JMX_PORT=7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN mkdir /kafka /data /logs  
  
ADD
http://www.eu.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}
/tmp/  
ADD
https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}.md5
/tmp/  
  
WORKDIR /tmp  
  
RUN echo VERIFY CHECKSUM: && \  
gpg --print-md MD5 ${KAFKA_RELEASE_ARCHIVE} 2>/dev/null && \  
cat ${KAFKA_RELEASE_ARCHIVE}.md5 && \  
tar -zx -C /kafka --strip-components=1 -f ${KAFKA_RELEASE_ARCHIVE} && \  
rm -rf kafka_* && \  
find /kafka/bin -type f -exec \  
sed -i 's/#!\/bin\/bash/#!\/bin\/sh/g' {} +  
  
ADD config /kafka/config  
ADD start.sh /start.sh  
  
ENV PATH /kafka/bin:$PATH  
WORKDIR /kafka  
  
EXPOSE 9092 ${JMX_PORT}  
VOLUME [ "/data", "/logs" ]  
  
CMD ["/start.sh"]  
  

