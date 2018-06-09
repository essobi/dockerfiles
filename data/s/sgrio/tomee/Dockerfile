FROM sgrio/java-oracle:jdk_7  
MAINTAINER SgrAlpha <admin@mail.sgr.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TOMEE_VERSION 7.0.4  
ENV APR_VERSION 1.6.3  
ENV TC_NATIVE_VERSION 1.2.16  
ENV OPENSSL_VERSION 1.0.2n  
  
ENV CATALINA_HOME /opt/apache-tomee-${TOMEE_VERSION}  
ENV PATH ${CATALINA_HOME}/bin:$PATH  
  
RUN curl --silent --location --retry 3 \  
http://archive.apache.org/dist/tomee/tomee-"${TOMEE_VERSION}"/apache-
tomee-"${TOMEE_VERSION}"-plus.tar.gz \  
| tar xz -C /tmp && \  
mv /tmp/apache-tomee-plus-${TOMEE_VERSION} ${CATALINA_HOME} && \  
rm -rf ${CATALINA_HOME}/bin/*.bat \  
${CATALINA_HOME}/bin/*.exe \  
${CATALINA_HOME}/bin/*.tar.gz \  
${CATALINA_HOME}/bin/*.original \  
${CATALINA_HOME}/conf/*.original \  
${CATALINA_HOME}/logs/* \  
${CATALINA_HOME}/temp/* \  
${CATALINA_HOME}/webapps/* \  
${CATALINA_HOME}/work/* && \  
ln -s ${CATALINA_HOME} /opt/apache-tomee && \  
apt-get update && apt-get install \  
gcc \  
libc6-dev \  
libssl-dev \  
libfile-dircompare-perl \  
make \  
-y --no-install-recommends && \  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GlobalSign_Root_CA.pem \  
https://www.openssl.org/source/openssl-"${OPENSSL_VERSION}".tar.gz \  
| tar xz -C /tmp && \  
cd /tmp/openssl-"${OPENSSL_VERSION}" && \  
./config --prefix=/usr && \  
make clean && make && make install && \  
curl --silent --location --retry 3 \  
http://archive.apache.org/dist/apr/apr-${APR_VERSION}.tar.gz \  
| tar xz -C /tmp && \  
cd /tmp/apr-${APR_VERSION} && \  
./configure && \  
make clean && make && make install && \  
curl --silent --location --retry 3 \  
http://archive.apache.org/dist/tomcat/tomcat-
connectors/native/${TC_NATIVE_VERSION}/source/tomcat-
native-${TC_NATIVE_VERSION}-src.tar.gz \  
| tar xz -C /tmp && \  
cd /tmp/tomcat-native-${TC_NATIVE_VERSION}-src/native && \  
./configure -with-apr=/usr/local/apr/ -with-ssl=/usr -with-java-
home=${JAVA_HOME} -prefix=${CATALINA_HOME} && \  
make clean && make && make install && \  
apt-get remove --purge --auto-remove -y \  
gcc \  
libc6-dev \  
libssl-dev \  
libfile-dircompare-perl \  
make && \  
apt-get autoclean && apt-get --purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LD_LIBRARY_PATH "${LD_LIBRARY_PATH}:${CATALINA_HOME}/lib"  
EXPOSE 8005 8080 8009 8443 45564 4000  
COPY files/bin/* ${CATALINA_HOME}/bin/  
COPY files/conf/* ${CATALINA_HOME}/conf/  
COPY files/ssl ${CATALINA_HOME}/ssl  
  
RUN openssl rand -hex 8 > ${CATALINA_HOME}/ssl/SSL_PASSWORD.txt && \  
openssl genrsa -out ${CATALINA_HOME}/ssl/localhost.key 2048 && \  
openssl req -config ${CATALINA_HOME}/ssl/openssl.cnf -new -key
${CATALINA_HOME}/ssl/localhost.key -out ${CATALINA_HOME}/ssl/localhost.csr &&
\  
openssl x509 -req -days 365 -in ${CATALINA_HOME}/ssl/localhost.csr -signkey
${CATALINA_HOME}/ssl/localhost.key -out ${CATALINA_HOME}/ssl/localhost.crt &&
\  
openssl pkcs12 -export -out ${CATALINA_HOME}/ssl/localhost.p12 -inkey
${CATALINA_HOME}/ssl/localhost.key -in ${CATALINA_HOME}/ssl/localhost.crt
-password pass:`cat ${CATALINA_HOME}/ssl/SSL_PASSWORD.txt` && \  
sed -i "s#SSL_FILE#ssl/localhost.p12#g" ${CATALINA_HOME}/conf/server.xml && \  
sed -i "s#SSL_PASSWORD#`cat ${CATALINA_HOME}/ssl/SSL_PASSWORD.txt`#g"
${CATALINA_HOME}/conf/server.xml && \  
rm ${CATALINA_HOME}/ssl/SSL_PASSWORD.txt  
  
WORKDIR ${CATALINA_HOME}  
  
CMD ${CATALINA_HOME}/bin/catalina.sh run  

