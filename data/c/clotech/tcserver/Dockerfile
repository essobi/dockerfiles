# build is-tcserver:latest  
# docker build tcserver -t is-tcserver:latest  
FROM centos:7  
EXPOSE 6969 8080 8443  
RUN yum install -y vim wget  
  
# install yum repo  
#RUN rpm --import http://packages.gopivotal.com/pub/rpm/rhel6/app-suite/RPM-
GPG-KEY-PIVOTAL-APP-SUITE-EL6  
RUN rpm --import http://packages.gopivotal.com/pub/rpm/rhel7/app-suite/RPM-
GPG-KEY-PIVOTAL-APP-SUITE-EL7  
RUN yum-config-manager --add-repo
http://packages.pivotal.io/pub/rpm/rhel7/app-suite/x86_64  
  
# install tcserver  
RUN yum install -y pivotal-tc-server-standard  
  
# add ojdbc6 and ojdbc7 to tomcat/lib directories  
ADD lib/ojdbc*.jar /tmp/  
RUN find /opt/pivotal/pivotal-tc-server-standard/tomcat-*.RELEASE -type d
-name 'lib' -exec cp /tmp/ojdbc7*.jar {} \;  
  
# install java, set JAVA_HOME  
RUN cd ~  
RUN wget -nv --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.rpm"  
RUN yum -y localinstall jdk-8u60-linux-x64.rpm  
RUN rm jdk-*.rpm  
ENV JAVA_HOME /usr/java/jdk1.8.0_60/jre  
  
  
# install tcserver instance (01)  
RUN mkdir -p /web/tcserver  
RUN /opt/pivotal/pivotal-tc-server-standard/tcruntime-instance.sh create -i
/web/tcserver 01  
  
# add default manager.war  
ADD webapps/manager.war /web/tcserver/01/webapps  
  
# start the tcserver instance  
RUN /web/tcserver/01/bin/tcruntime-ctl.sh start /web/tcserver/01  
  
# keep the container alive (PID=1)  
CMD tail -f /web/tcserver/01/logs/catalina.out  
#ENTRYPOINT tail -f /dev/null  

