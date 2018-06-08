FROM centos:centos7  
  
ENV SONATYPE_WORK /opt/nexus/data  
ENV NEXUS_VERSION 3.0.0-b2016011501  
  
RUN yum install -y \  
curl tar createrepo \  
&& yum clean all  
  
RUN cd /var/tmp \  
&& curl \--fail \--silent \--location \--retry 3 -O \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie; " \  
http://download.oracle.com/otn-pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.rpm \  
&& rpm -Ui jdk-8u60-linux-x64.rpm \  
&& rm -rf jdk-8u60-linux-x64.rpm  
  
RUN curl \--fail \--silent \--location \--retry 3 \  
http://download.sonatype.com/nexus/3/nexus-3.0.0-m7-unix.tar.gz \  
| gunzip \  
| tar x -C /tmp nexus-${NEXUS_VERSION} \  
&& mv -T /tmp/nexus-${NEXUS_VERSION}/ /opt/nexus/  
  
  
RUN mkdir -p /opt/nexus/etc/ssl  
  
RUN echo $'Password\n\  
Password\n\  
Name Name\n\  
ou\n\  
company.com\n\  
Vienna\n\  
Vienna\n\  
at\n\  
yes\n\  
Password\n\  
Password\n'\  
> /opt/nexus/etc/ssl/keystore.conf  
  
RUN keytool -keystore /opt/nexus/etc/ssl/keystore.jks -alias anecon.com
-genkey -keyalg RSA < /opt/nexus/etc/ssl/keystore.conf  
  
RUN useradd -r -u 200 -m -c "nexus role account" -d ${SONATYPE_WORK} -s
/bin/false nexus \  
&& chown -R nexus /opt/nexus  
  
RUN sed -i 's/^nexus-args=.*/nexus-
args=${karaf.base}\/etc\/jetty.xml,${karaf.base}\/etc\/jetty-
requestlog.xml,${karaf.base}\/etc\/jetty-https.xml/g'
/opt/nexus/etc/custom.properties \  
&& echo "application-port-ssl=8443" >> /opt/nexus/etc/org.sonatype.nexus.cfg \  
&& sed -i 's/<Set name="KeyStorePath">.*<\/Set>/<Set
name="KeyStorePath">\/opt\/nexus\/etc\/ssl\/keystore.jks<\/Set>/g'
/opt/nexus/etc/jetty-https.xml \  
&& sed -i 's/<Set name="KeyStorePassword">.*<\/Set>/<Set
name="KeyStorePassword">Password<\/Set>/g' /opt/nexus/etc/jetty-https.xml \  
&& sed -i 's/<Set name="KeyManagerPassword">.*<\/Set>/<Set
name="KeyManagerPassword">Password<\/Set>/g' /opt/nexus/etc/jetty-https.xml \  
&& sed -i 's/<Set name="TrustStorePath">.*<\/Set>/<Set
name="TrustStorePath">\/opt\/nexus\/etc\/ssl\/keystore.jks<\/Set>/g'
/opt/nexus/etc/jetty-https.xml \  
&& sed -i 's/<Set name="TrustStorePassword">.*<\/Set>/<Set
name="TrustStorePassword">Password<\/Set>/g' /opt/nexus/etc/jetty-https.xml  
  
VOLUME ${SONATYPE_WORK}  
  
# http, https, https for docker  
EXPOSE 8081 8443 18443  
WORKDIR /opt/nexus  
USER nexus  
ENTRYPOINT ["/opt/nexus/bin/nexus", "run"]  

