FROM mosaicoon/java-8-alpine-bash  
  
ENV SOFTWARE_DIR kafka-manager  
ENV TEMP_DIR /tmp  
ENV APPLICATION_SECRET
"^<csmm5Fx4d=r2HEX8pelM3iBkFVv?k[mc;IZE<_Qoq8EkX_/7@Zh73P05Pzea3U"  
ENV ZK_HOSTS zookeeper:2181  
  
RUN mkdir -p "${TEMP_DIR}"/"${SOFTWARE_DIR}"/ && \  
cd "${TEMP_DIR}"/"${SOFTWARE_DIR}"/ && \  
apk add \--update wget && \  
wget \--no-check-certificate https://github.com/yahoo/kafka-
manager/archive/master.zip && \  
unzip ./master.zip && \  
rm -f master.zip && \  
  
mkdir -p "${TEMP_DIR}"/"${SOFTWARE_DIR}"/kafka-manager-master/ && \  
cd "${TEMP_DIR}"/"${SOFTWARE_DIR}"/kafka-manager-master/ && \  
echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt && \  
./sbt clean dist && \  
apk del wget && \  
  
mkdir -p /usr/src/"${SOFTWARE_DIR}"/ && \  
cd /usr/src/"${SOFTWARE_DIR}"/ && \  
mv "${TEMP_DIR}"/"${SOFTWARE_DIR}"/kafka-manager-
master/target/universal/kafka-manager-*.zip . && \  
mv "${TEMP_DIR}"/"${SOFTWARE_DIR}"/kafka-manager-master/conf/application.conf
. && \  
rm -rf "${TEMP_DIR}"/"${SOFTWARE_DIR}" && \  
unzip ./kafka-manager-*.zip && \  
rm -rf ./kafka-manager-*.zip && \  
mv kafka-manager-* ./kafka-manager  
  
WORKDIR /usr/src/"${SOFTWARE_DIR}"/kafka-manager  
  
EXPOSE 9000  
  
CMD ./bin/kafka-manager
-Dconfig.file=/usr/src/"${SOFTWARE_DIR}"/application.conf

