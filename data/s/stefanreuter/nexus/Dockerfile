FROM openjdk:jre  
MAINTAINER Stefan Reuter <docker@reucon.com>  
  
ENV VERSION 2.14.5-02  
ENV DUMB_INIT_VERSION 1.2.1  
ENV SONATYPE_WORK /sonatype-work  
ENV RUN_USER nexus  
ENV RUN_GROUP nexus  
  
ADD https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 /usr/local/bin/dumb-init  
  
RUN set -x \  
&& chmod +x /usr/local/bin/dumb-init \  
&& useradd -r -u 200 -m -c "Nexus role account" -d ${SONATYPE_WORK} -s
/bin/false ${RUN_USER} \  
&& curl --fail --silent --location --retry 3 \  
https://download.sonatype.com/nexus/oss/nexus-${VERSION}-bundle.tar.gz \  
| tar xz -C /opt \  
&& mv /opt/nexus-${VERSION} /opt/nexus \  
&& rm -rf /opt/nexus/nexus/WEB-INF/plugin-repository/nexus-outreach-plugin-* \  
&& chown -R ${RUN_USER}:${RUN_GROUP} /opt/nexus  
  
VOLUME ${SONATYPE_WORK}  
  
EXPOSE 8081  
WORKDIR /opt/nexus  
USER ${RUN_USER}  
  
ENTRYPOINT ["/usr/local/bin/dumb-init"]  
CMD ["/usr/bin/java", \  
"-Dnexus-work=/sonatype-work", \  
"-Dnexus-webapp-context-path=/", \  
"-Dnexus.remoteStorage.enableCircularRedirectsForHosts=maven.oracle.com,www.oracle.com,login.oracle.com,oracle.com",
\  
"-Dnexus.remoteStorage.useCookiesForHosts=maven.oracle.com,www.oracle.com,login.oracle.com,oracle.com",
\  
"-Xms768m", \  
"-Xmx768m", \  
"-cp", "conf/:lib/*", \  
"org.sonatype.nexus.bootstrap.Launcher", \  
"./conf/jetty.xml", \  
"./conf/jetty-requestlog.xml"]  

