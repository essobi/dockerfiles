FROM cakkineni/oss-base  
  
RUN yum -y update; yum clean all; yum -y install bash curl sed
java-1.8.0-openjdk.x86_64 which classpath  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisor.conf  
  
#ENV SDC_USER=sdc  
# The paths below should generatelly be attached to a VOLUME for persistence  
# SDC_DATA is a volume for storing collector state. Do not share this between
containers.  
# SDC_LOG is an optional volume for file based logs. You must provide a custom
sdc-log4j.properties file to use this.  
# SDC_CONF is where configuration files are stored. This can be shared.  
# SDC_RESOURCES is where resource files such as runtime:conf resources and
Hadoop configuration can be placed.  
ENV SDC_DIST="/opt/streamsets-datacollector" \  
SDC_DATA=/data \  
SDC_LOG=/logs \  
SDC_CONF=/etc/sdc \  
SDC_RESOURCES=/resources  
# STREAMSETS_LIBRARIES_EXTRA_DIR is where extra libraries such as JDBC drivers
should go.  
ENV STREAMSETS_LIBRARIES_EXTRA_DIR="${SDC_DIST}/libs-common-lib"  
#RUN useradd -r -U ${SDC_USER}  
# ARG is new in Docker 1.9 and not yet supported by Docker Hub Automated
Builds  
# ARG SDC_VERSION  
ENV SDC_VERSION ${SDC_VERSION:-1.5.0.0}  
  
# Download the SDC tarball, Extract tarball and cleanup  
RUN cd /tmp && \  
curl -O -L
"https://archives.streamsets.com/datacollector/${SDC_VERSION}/tarball/streamsets-
datacollector-core-${SDC_VERSION}.tgz" && \  
tar xzf "/tmp/streamsets-datacollector-core-${SDC_VERSION}.tgz" -C /opt/ && \  
cd /opt/streamsets-datacollector-${SDC_VERSION} && sed -i 's/run sha1sum
-s/run sha1sum/g' libexec/_stagelibs && \  
cd /opt/streamsets-datacollector-${SDC_VERSION} && bin/streamsets stagelibs
-install=streamsets-datacollector-rabbitmq-lib,streamsets-datacollector-
apache-kafka_0_8_2-lib,streamsets-datacollector-redis-lib && \  
rm -rf "/tmp/streamsets-datacollector-core-${SDC_VERSION}.tgz" && \  
mv "/opt/streamsets-datacollector-${SDC_VERSION}" "${SDC_DIST}"  
  
# Log to stdout for docker instead of sdc.log for compatibility with docker.  
#RUN sed -i 's|DEBUG|INFO|' "${SDC_DIST}/etc/sdc-log4j.properties" && \  
#sed -i 's|INFO, streamsets|INFO, stdout|' "${SDC_DIST}/etc/sdc-
log4j.properties"  
# Create data directory and optional mount point  
RUN mkdir -p "${SDC_DATA}" /mnt "${SDC_LOG}" "${SDC_RESOURCES}"  
  
# Move configuration to /etc/sdc  
RUN mv "${SDC_DIST}/etc" "${SDC_CONF}"  
  
# Disable authentication by default, overriable with custom sdc.properties.  
RUN sed -i 's|\\(http.authentication=\\).*|\1none|'
"${SDC_CONF}/sdc.properties"  
  
#sha1sum on centos doesnt use -s option used in the following script  
#RUN cd ${SDC_DIST} && sed -i 's/run sha1sum -s/run sha1sum/g'
libexec/_stagelibs  
# Setup filesystem permissions  
#RUN chown -R "${SDC_USER}:${SDC_USER}" "${SDC_CONF}" "${SDC_DATA}"
"${SDC_LOG}" "${SDC_RESOURCES}"  
#USER ${SDC_USER}  
EXPOSE 18630 2003/udp 5140/udp  
ADD streamsets-init.sh /tmp/streamsets-init.sh  
RUN chmod +x /tmp/streamsets-init.sh  

