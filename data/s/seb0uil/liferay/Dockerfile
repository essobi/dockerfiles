FROM centos:6.6  
MAINTAINER seb0uil  
  
ENV JAVA_URL=http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz  
ENV JAVA_VERSION=jdk1.7.0_79  
  
ENV
LF_URL=http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-
portal-jboss-6.2-ce-
ga6-20160112152609836.zip?r=&ts=1453814463&use_mirror=skylink  
ENV LF_VERSION=liferay-portal-6.2-ce-ga6  
  
ENV ANT_URL=http://apache.crihan.fr/dist/ant/binaries/apache-
ant-1.9.6-bin.tar.gz  
ENV ANT_VERSION=apache-ant-1.9.6  
ENV
ECJ_URL=http://central.maven.org/maven2/org/eclipse/jdt/core/compiler/ecj/4.4.2/ecj-4.4.2.jar  
  
#Install LF  
ADD custom.sh /tmp/custom.sh  
ADD bashrc /root/.bashrc  
  
RUN mkdir -p /opt/liferay/ \  
&& yum -y install tar unzip git svn wget \  
&& wget "${LF_URL}" -O /tmp/liferay.zip \  
&& unzip /tmp/liferay.zip -d /opt/liferay/ \  
&& ln -s ${LF_VERSION} /opt/liferay/current \  
&& cp /tmp/custom.sh /opt/liferay/current/jboss-7.1.1/bin/custom.sh \  
&& chmod +x /opt/liferay/current/jboss-7.1.1/bin/custom.sh \  
&& (echo && echo JAVA_OPTS=\"\$JAVA_OPTS -Djboss.bind.address=0.0.0.0 -Xmx3G
-XX:MaxPermSize=1G
-Xrunjdwp:transport=dt_socket,address=8787,server=y,suspend=n\" && echo
JAVA_HOME=\"/opt/java/current\" && echo eval \$DIRNAME/custom.sh) >>
/opt/liferay/current/jboss-7.1.1/bin/standalone.conf \  
&& mkdir -p /opt/java \  
&& wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" ${JAVA_URL} -O /tmp/jdk.tar.gz \  
&& tar xvzf /tmp/jdk.tar.gz -C /opt/java/ \  
&& ln -s ${JAVA_VERSION} /opt/java/current \  
&& yum -y clean all \  
&& mkdir -p /opt/ant/ \  
&& wget "${ANT_URL}" -O /tmp/ant.tar.gz \  
&& tar xvzf /tmp/ant.tar.gz -C /opt/ant \  
&& ln -s ${ANT_VERSION} /opt/ant/current \  
&& rm -f /tmp/ant.tar.gz \  
&& wget "${ECJ_URL}" -O /opt/ant/current/lib/ecj.jar \  
&& rm -rf /tmp/*  
  
ADD portal-setup-wizard.properties /opt/liferay/current/portal-setup-
wizard.properties  
  
ADD svn.sh /tmp/svn.sh  
RUN chmod +x /tmp/svn.sh  
  
EXPOSE 8080  
EXPOSE 22  
EXPOSE 8787  
VOLUME /deploy  
VOLUME /data  
  
CMD ["/bin/bash" ,"-x", "/tmp/svn.sh"]  

