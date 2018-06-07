FROM alpine:3.6  
ENV CTMPL_VERSION 0.19.4  
RUN set -x \  
&& apk add --no-cache --virtual .install-deps ca-certificates gnupg openssl \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
91A6E7F85D05C65630BEF18951852D87348FFC4C \  
&& wget https://releases.hashicorp.com/consul-
template/${CTMPL_VERSION}/consul-template_${CTMPL_VERSION}_linux_amd64.zip \  
&& wget https://releases.hashicorp.com/consul-
template/${CTMPL_VERSION}/consul-template_${CTMPL_VERSION}_SHA256SUMS \  
&& wget https://releases.hashicorp.com/consul-
template/${CTMPL_VERSION}/consul-template_${CTMPL_VERSION}_SHA256SUMS.sig \  
&& gpg --batch --verify consul-template_${CTMPL_VERSION}_SHA256SUMS.sig
consul-template_${CTMPL_VERSION}_SHA256SUMS \  
&& grep consul-template_${CTMPL_VERSION}_linux_amd64.zip consul-
template_${CTMPL_VERSION}_SHA256SUMS | sha256sum -c \  
&& unzip -d /bin consul-template_${CTMPL_VERSION}_linux_amd64.zip \  
&& rm -rf consul-template_* /root/.gnupg \  
&& apk del .install-deps  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.82  
RUN set -x \  
&& adduser -D -u 1000 tomcat \  
&& tomcat_archive=apache-tomcat-${TOMCAT_VERSION}.tar.gz \  
&& apk add --no-cache su-exec dumb-init \  
&& apk add --no-cache --virtual .install-deps \  
ca-certificates \  
gnupg \  
openssl \  
tar \  
&& wget
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/${tomcat_archive}
\  
&& wget
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/${tomcat_archive}.asc
\  
&& wget https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/KEYS \  
&& gpg --import KEYS \  
&& gpg --batch --verify ${tomcat_archive}.asc ${tomcat_archive} \  
&& tar -xf ${tomcat_archive} \--strip-components=1 \  
&& rm -rf webapps/* logs/* \  
&& mkdir -p conf/Catalina \  
&& mv conf/server.xml conf/server.xml.original \  
&& mv conf/tomcat-users.xml conf/tomcat-users.xml.original \  
&& rm -rf ${tomcat_archive} ${tomcat_archive}.asc KEYS /root/.gnupg \  
&& apk del .install-deps  
  
ENV TOMCAT_HTTP_PORT=8080 \  
TOMCAT_JMX_PORT=1099 \  
JPDA_ADDRESS=8000  
COPY tomcat $CATALINA_HOME/  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE $TOMCAT_HTTP_PORT $TOMCAT_JMX_PORT $JPDA_ADDRESS  
  
CMD ["catalina.sh", "run"]  

