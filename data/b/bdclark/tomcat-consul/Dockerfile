FROM buildpack-deps:jessie-curl  
  
ENV DUMB_INIT_VERSION 1.2.0  
RUN set -x \  
&& wget --no-verbose "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb" \  
&& wget --no-verbose "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/sha256sums" \  
&& grep "dumb-init_${DUMB_INIT_VERSION}_amd64.deb" sha256sums | sha256sum -c \  
&& rm sha256sums \  
&& dpkg -i dumb-init_*.deb \  
&& rm -rf dumb-init_*.deb  
  
# ENV GOSU_VERSION 1.10  
# RUN set -x \  
# && wget --no-verbose -O /usr/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
# && wget --no-verbose -O /usr/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
# && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
# && gpg --batch --verify /usr/bin/gosu.asc /usr/bin/gosu \  
# && rm -rf /root/.gnupg /usr/bin/gosu.asc \  
# && chmod +x /usr/bin/gosu \  
# && gosu nobody true  
ENV CTMPL_VERSION 0.18.1  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends unzip \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
91A6E7F85D05C65630BEF18951852D87348FFC4C \  
&& wget --no-verbose https://releases.hashicorp.com/consul-
template/${CTMPL_VERSION}/consul-template_${CTMPL_VERSION}_linux_amd64.zip \  
&& wget --no-verbose https://releases.hashicorp.com/consul-
template/${CTMPL_VERSION}/consul-template_${CTMPL_VERSION}_SHA256SUMS \  
&& wget --no-verbose https://releases.hashicorp.com/consul-
template/${CTMPL_VERSION}/consul-template_${CTMPL_VERSION}_SHA256SUMS.sig \  
&& gpg --batch --verify consul-template_${CTMPL_VERSION}_SHA256SUMS.sig
consul-template_${CTMPL_VERSION}_SHA256SUMS \  
&& grep consul-template_${CTMPL_VERSION}_linux_amd64.zip consul-
template_${CTMPL_VERSION}_SHA256SUMS | sha256sum -c \  
&& unzip -d /usr/bin consul-template_${CTMPL_VERSION}_linux_amd64.zip \  
&& rm -rf consul-template_* /root/.gnupg /var/lib/apt/lists/*  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.76  
RUN set -x \  
&& useradd --uid 1000 tomcat \  
&& tomcat_archive=apache-tomcat-${TOMCAT_VERSION}.tar.gz \  
&& wget --no-verbose
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/${tomcat_archive}
\  
&& wget --no-verbose
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/${tomcat_archive}.asc
\  
&& wget --no-verbose
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/KEYS \  
&& gpg --import KEYS \  
&& gpg --batch --verify ${tomcat_archive}.asc ${tomcat_archive} \  
&& tar -xf ${tomcat_archive} \--strip-components=1 \  
&& rm -rf webapps/* logs/* \  
&& mkdir -p conf/Catalina \  
&& mv conf/server.xml conf/server.xml.original \  
&& mv conf/tomcat-users.xml conf/tomcat-users.xml.original \  
&& rm -rf ${tomcat_archive} ${tomcat_archive}.asc KEYS /root/.gnupg  
  
ENV TOMCAT_PREFIX="service/tomcat" \  
TOMCAT_HTTP_PORT=8080 \  
TOMCAT_JMX_PORT=9080 \  
JPDA_ADDRESS=9180 \  
TOMCAT_JMX_AUTHENTICATE=true \  
TOMCAT_JMX_ACCESS_FILE=$CATALINA_HOME/conf/jmxremote.access \  
TOMCAT_JMX_PASSWORD_FILE=$CATALINA_HOME/conf/jmxremote.password  
  
COPY tomcat $CATALINA_HOME/  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE $TOMCAT_HTTP_PORT $TOMCAT_JMX_PORT $JPDA_ADDRESS  
  
CMD ["catalina.sh", "run"]  

