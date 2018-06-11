FROM centos:6.6  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6  
  
#ENV JAVA_VERSION 8u31  
#ENV BUILD_VERSION b13  
RUN yum update -y  
RUN yum -y install wget tar which  
  
#RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O
/tmp/jdk-8-linux-x64.rpm  
COPY jdk-8u31-linux-x64.rpm /tmp/  
RUN yum -y install /tmp/jdk-8u31-linux-x64.rpm  
  
RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000  
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
  
ENV JAVA_HOME /usr/java/latest  
RUN echo 'export JAVA_HOME="${JAVA_HOME}"' >> ~/.bashrc  
  
#ENV TOMCAT_MAJOR 8  
#ENV TOMCAT_VERSION 8.0.30  
#ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
#RUN wget --no-cookies --no-check-certificate "${TOMCAT_TGZ_URL}" -O
/tmp/tomcat.tar.gz \  
# && tar -xvf /tmp/tomcat.tar.gz -C /opt \  
# && ln -s /opt/apache-tomcat-8.0.30 /opt/tomcat  
COPY apache-tomcat-8.0.30.tar.gz /tmp/  
RUN tar -xvf /tmp/apache-tomcat-8.0.30.tar.gz -C /opt \  
&& ln -s /opt/apache-tomcat-8.0.30 /opt/tomcat  
  
EXPOSE 8080  
# Clean up when done  
RUN rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  
  
CMD /opt/tomcat/bin/catalina.sh run  

