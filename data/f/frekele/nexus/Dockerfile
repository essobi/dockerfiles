FROM frekele/java:jdk8  
  
MAINTAINER frekele <leandro.freitas@softdevelop.com.br>  
  
ENV NEXUS_VERSION=3.9.0-01  
ENV NEXUS_HOME=/opt/sonatype/nexus  
ENV NEXUS_DATA=/nexus-data  
ENV NEXUS_CONTEXT=''  
ENV JAVA_MAX_MEM=1024m  
ENV JAVA_MIN_MEM=256m  
ENV EXTRA_JAVA_OPTS=""  
# Change to tmp folder  
WORKDIR /tmp  
  
# Download and extract apache ant to opt folder  
RUN mkdir -p ${NEXUS_HOME} \  
&& wget --no-check-certificate --no-cookies
http://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz \  
&& wget --no-check-certificate --no-cookies
http://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz.md5 \  
&& echo "$(cat nexus-${NEXUS_VERSION}-unix.tar.gz.md5)
nexus-${NEXUS_VERSION}-unix.tar.gz" | md5sum -c \  
&& tar -zvxf nexus-${NEXUS_VERSION}-unix.tar.gz --strip-components=1 -C
${NEXUS_HOME} \  
&& rm -f nexus-${NEXUS_VERSION}-unix.tar.gz \  
&& rm -f nexus-${NEXUS_VERSION}-unix.tar.gz.md5 \  
&& chown -R root:root ${NEXUS_HOME}  
  
# Configure Nexus  
RUN sed -e "s|karaf.home=.|karaf.home=${NEXUS_HOME}|g" \  
-e "s|karaf.base=.|karaf.base=${NEXUS_HOME}|g" \  
-e "s|karaf.etc=etc|karaf.etc=${NEXUS_HOME}/etc|g" \  
-e "s|java.util.logging.config.file=etc|java.util.logging.config.file=${NEXUS_HOME}/etc|g" \  
-e "s|karaf.data=.*|karaf.data=${NEXUS_DATA}|g" \  
-e "s|java.io.tmpdir=.*|java.io.tmpdir=${NEXUS_DATA}/tmp|g" \  
-e "s|LogFile=.*|LogFile=${NEXUS_DATA}/log/jvm.log|g" \  
-i ${NEXUS_HOME}/bin/nexus.vmoptions \  
&& sed -e "s|nexus-context-path=/|nexus-context-path=/${NEXUS_CONTEXT}|g" \  
-i ${NEXUS_HOME}/etc/nexus-default.properties \  
&& mkdir -p ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp  
  
# Fix for issue https://issues.sonatype.org/browse/NEXUS-10049  
RUN touch ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.feature.cfg \  
&& touch ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.system.cfg \  
&& touch ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.bundle.cfg \  
&& touch ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.shell.cfg \  
&& touch ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.config.cfg \  
&& touch ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.jaas.cfg  
  
# Create nexus user with UID 200  
RUN useradd -r -u 200 -m -c "nexus role account" -d ${NEXUS_DATA} -s
/bin/false nexus  
  
# Add Volume  
VOLUME ${NEXUS_DATA}  
  
# Open Port  
EXPOSE 8081  
# Add the files  
ADD rootfs /  
  
# Change to root folder  
WORKDIR /root  

