FROM mcapitanio/centos-java  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
USER root  
  
ENV SCHEMA_REGISTRY_VER 3.0.1  
ENV COMMON_VER 3.1.0  
ARG httpProxyHost  
ARG httpProxyPort  
  
ENV http_proxy ${http_proxy}  
ENV https_proxy ${https_proxy}  
ENV no_proxy ${no_proxy}  
ENV httpProxyHost ${httpProxyHost}  
ENV httpProxyPort ${httpProxyPort}  
  
ENV SCHEMA_REGISTRY_HOME /opt/schema-registry  
  
ENV PATH $SCHEMA_REGISTRY_HOME/bin:$PATH  
  
# Install needed packages  
RUN yum update -y; \  
yum clean all  
RUN yum install -y git \  
maven \  
python-pip \  
python-setuptools  
RUN yum clean all  
RUN easy_install supervisor  
  
WORKDIR /opt/docker  
  
RUN mkdir /root/.m2  
COPY settings.xml ./  
COPY set-maven-proxy.sh ./  
RUN chmod +x set-maven-proxy.sh  
RUN ./set-maven-proxy.sh  
  
# Confluent Schema Registry  
RUN git clone -b v$SCHEMA_REGISTRY_VER https://github.com/confluentinc/schema-
registry.git  
RUN cd schema-registry; \  
mvn clean package -DskipTests  
RUN mv schema-registry/package-schema-registry/target/kafka-schema-registry-
package-$SCHEMA_REGISTRY_VER-package $SCHEMA_REGISTRY_HOME  
  
# Confluent Common  
RUN git clone -b common-$COMMON_VER https://github.com/confluentinc/common.git  
RUN cd common; \  
mvn clean package -DskipTests  
RUN cp -Rf common/package/target/common-package-$COMMON_VER-SNAPSHOT-
package/share $SCHEMA_REGISTRY_HOME/  
  
# Confluent Rest Utils  
RUN git clone -b v$SCHEMA_REGISTRY_VER https://github.com/confluentinc/rest-
utils.git  
RUN cd rest-utils; \  
mvn clean package -DskipTests  
RUN cp -Rf rest-utils/package/target/rest-utils-package-$SCHEMA_REGISTRY_VER-
package/share $SCHEMA_REGISTRY_HOME/  
  
ADD schema-registry/ $SCHEMA_REGISTRY_HOME/  
RUN chmod +x $SCHEMA_REGISTRY_HOME/bin/supervisord-bootstrap.sh; \  
chmod +x $SCHEMA_REGISTRY_HOME/bin/start-schema-registry.sh; \  
mkdir $SCHEMA_REGISTRY_HOME/logs  
  
COPY etc/ /etc/  
  
EXPOSE 8081  
VOLUME [ "/opt/schema-registry/etc/schema-registry", "/opt/schema-
registry/logs" ]  
  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

