FROM debian:stretch  
MAINTAINER Marc Richter <mail@marc-richter.info>  
  
# setup useful environment variables  
ENV CONF_VERSION 6.8.1  
ENV CONF_INST /usr/local/atlassian/confluence  
ENV CONF_HOME ${CONF_INST}-data  
ENV CONF_SETENV ${CONF_INST}/bin/setenv.sh  
ENV PG_VERSION 9.6  
ENV JAVA_VERSION 1.8.0_162  
ENV JAVA_VERSION_SHORT 8u162  
ENV JAVA_VERSION_FULL ${JAVA_VERSION_SHORT}-b12  
ENV JAVA_MD5 0da788060d494f5095bf8624735fa2f1  
ENV JAVA_HOME /opt/jdk/jdk${JAVA_VERSION}  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update System and install necessary packages  
RUN set -x \  
&& apt-get update -q \  
&& apt-get dist-upgrade -y -q \  
&& apt-get install -y -q apt-utils \  
&& apt-get install -y -q postgresql-${PG_VERSION} postgresql-client wget curl
locales-all  
# Create needed folders  
RUN set -x \  
&& mkdir -p "${CONF_HOME}" "${CONF_INST}"  
# Prepare PostgreSQL  
RUN set -x \  
&& pg_dropcluster ${PG_VERSION} main \  
&& pg_createcluster --locale='en_US.UTF-8' ${PG_VERSION} main \  
&& sed -i'' 's/peer/trust/g' /etc/postgresql/${PG_VERSION}/main/pg_hba.conf \  
&& sed -i'' 's/md5/trust/g' /etc/postgresql/${PG_VERSION}/main/pg_hba.conf \  
&& pg_ctlcluster ${PG_VERSION} main start -- -w \  
&& /usr/bin/psql -U postgres -c "CREATE DATABASE confluence ENCODING =
'UTF8';" \  
&& pg_ctlcluster ${PG_VERSION} main stop -- -m fast  
  
COPY startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
# Grab Confluence, extract it and prepare folders and configs  
RUN set -x \  
&& curl -Ls
"https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz" \  
| tar -xz --directory "${CONF_INST}/" \--strip-components=1 \  
&& chmod -R 777 "${CONF_INST}/temp" \  
&& chmod -R 777 "${CONF_INST}/logs" \  
&& chmod -R 777 "${CONF_INST}/work" \  
&& echo -e "\nconfluence.home=${CONF_HOME}" >> "${CONF_INST}/confluence/WEB-
INF/classes/confluence-init.properties"  
# Tune Confluence Settings  
RUN set -x \  
&& sed -i'' 's#Xmx1024m#Xmx2048m#g' ${CONF_SETENV}  
  
# Install Oracle JDK  
RUN mkdir -p /opt/jdk \  
&& wget -q --header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_FULL}/${JAVA_MD5}/jdk-${JAVA_VERSION_SHORT}-linux-x64.tar.gz
-O - \  
| tar xfz - -C /opt/jdk  
RUN update-alternatives --install /usr/bin/java java
/opt/jdk/jdk${JAVA_VERSION}/bin/java 100  
RUN update-alternatives --install /usr/bin/javac javac
/opt/jdk/jdk${JAVA_VERSION}/bin/javac 100  
  
EXPOSE 8090  
EXPOSE 8080  
CMD ["/startup.sh"]  

